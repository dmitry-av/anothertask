from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


class FirstView(TemplateView):
    template_name = 'first.html'


class SecondView(TemplateView):
    template_name = 'second.html'
