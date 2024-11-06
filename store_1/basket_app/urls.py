from django.urls import path
from basket_app import views

app_name = 'basket_app'

urlpatterns = [
    path('basket_add/<slug:product_slug>/', views.basket_add, name='basket_add'),
    path('basket_plus/<int:basket_id>/', views.basket_plus, name='basket_plus'),
    path('basket_minus/<int:basket_id>/', views.basket_minus, name='basket_minus'),
    path('basket_remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]