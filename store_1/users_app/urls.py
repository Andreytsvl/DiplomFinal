from django.urls import path
from users_app import views

app_name = 'users_app'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('users-basket/', views.users_basket, name='users_basket'),
    path('logout/', views.logout, name='logout'),

]