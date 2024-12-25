from django.urls import path

from pharmacy import views

app_name = 'pharmacy'

urlpatterns = [
    path('pharmacy-list/', views.pharmacy_list, name='pharmacy_list'),
]