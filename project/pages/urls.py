from django.urls import path
from .views import home, about, form


urlpatterns = [
    path('',home, name='home'),
    path('about',about, name='about'),
    path('form',form, name='form'),


]