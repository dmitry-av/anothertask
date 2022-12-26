from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=20, verbose_name='Menu title')
    slug = models.SlugField(
        max_length=255, verbose_name='Slug', null=True)  # use in template tag
    named_url = models.CharField(
        max_length=255, verbose_name='Named URL', blank=True)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        return self.title

    def get_path(self):
        if self.named_url:
            url = reverse(self.named_url)
        else:
            url = f'/{self.slug}/'
        return url


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items',
                             verbose_name='menu', blank=True, null=True,
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='items',
                               verbose_name='parent menu item',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Item title')
    url = models.CharField(max_length=255, verbose_name='Link', blank=True)
    named_url = models.CharField(
        max_length=255, verbose_name='Named URL', blank=True)

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'

    def get_url(self):
        if self.named_url:
            url = reverse(self.named_url)
        elif self.url:
            url = self.url
        else:
            url = '/'

        return url

    def __str__(self):
        return self.title
