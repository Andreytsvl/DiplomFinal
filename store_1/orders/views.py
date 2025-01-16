from django.contrib import messages
from django.http import JsonResponse
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
#from django.core.exceptions import ValidationError
from django.urls import reverse
import logging

from basket_app.models import Basket
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from pharmacy.models import Pharmacy
from products_app.models import Products


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    basket_items = Basket.objects.filter(user=user)

                    if basket_items.exists():
                        # Создаем заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            pharmacy=form.cleaned_data['pharmacy'],
                            payment_on_get=False,  # По умолчанию оплата картой
                            is_paid=False,  # Заказ не оплачен
                            status='Ожидает оплаты',  # Статус заказа
                        )

                        # Создать заказанные товары
                        for basket_item in basket_items:
                            product = basket_item.product
                            name = basket_item.product.name
                            price = basket_item.product.retail_price()
                            quantity = basket_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(
                                    f'Недостаточное количество товара {name} на складе. '
                                    f'В наличии - {product.quantity}'
                                )

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # Очистить корзину пользователя после создания заказа

                        # basket_items.delete()

                        # Перенаправляем на страницу выбора способа оплаты
                        return redirect('orders:select_payment', order_id=order.id)
                    else:
                        messages.error(request, 'Ваша корзина пуста.')
                        return redirect('basket:order')
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('basket:order')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        initial = {
            'phone_number': request.user.phone_number,
        }
        form = CreateOrderForm(initial=initial)

    pharmacies = Pharmacy.objects.all()
    context = {
        'title': 'Home - Оформление заказа',
        'form': form,
        'order': True,
        'pharmacies': pharmacies,
    }
    return render(request, 'orders/create_order.html', context=context)



@login_required
def select_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')

        if payment_method == 'card':
            # Перенаправляем на страницу оплаты картой
            return redirect('orders:payment_process', order_id=order.id)
        elif payment_method == 'on_get':
            # Обновляем заказ на "оплата при получении"
            order.payment_on_get = True
            order.status = 'Ожидает оплаты'
            order.save()
            # Очищаем корзину пользователя
            Basket.objects.filter(user=request.user).delete()

            messages.success(request, 'Заказ оформлен! Оплата при получении.')
            return redirect('user:profile')
        else:
            messages.error(request, 'Неверный способ оплаты.')
            return redirect('orders:select_payment', order_id=order.id)

    return render(request, 'orders/select_payment.html', {'order': order})


@login_required
def payment_process(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == 'POST':
        # Имитация успешной оплаты
        card_number = request.POST.get('card-number', '').replace(' ', '')
        if card_number == '4242424242424242':
            # Обновляем заказ на "оплачен"
            order.is_paid = True
            order.status = 'Оплачен'
            order.save()

            # Очищаем корзину пользователя
            Basket.objects.filter(user=request.user).delete()

            messages.success(request, 'Оплата прошла успешно! Заказ создан.')
            return redirect('user:profile')
        else:
            messages.error(request, 'Ошибка оплаты. Проверьте данные карты.')
            return redirect('orders:payment_process', order_id=order.id)

    return render(request, 'orders/payment_process.html', {'order': order})

# def payment_process(request):
#
#     return render(request, 'orders/payment_process.html')