from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    path('select-payment/<int:order_id>/', views.select_payment, name='select_payment'),  # Новый путь
    path('payment-process/<int:order_id>/', views.payment_process, name='payment_process'),  # Путь для оплаты
]