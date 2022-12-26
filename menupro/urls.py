from django.urls import path
from django.contrib import admin
from menuapp.views import HomeView, FirstView, SecondView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('first/', FirstView.as_view(), name='first'),
    path('second/', SecondView.as_view(), name='second'),
]
