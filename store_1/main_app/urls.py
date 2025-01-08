from django.urls import path
from django.views.decorators.cache import cache_page
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('',  views.index, name='index'),
    path('about/', cache_page(60*2)(views.about), name='about'),
]