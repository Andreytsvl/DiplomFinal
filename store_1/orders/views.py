from django.contrib import messages
from django.http import JsonResponse
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
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
        #logger = logging.getLogger(__name__)

        # form = CreateOrderForm(data=request.POST)
        # if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    basket_items = Basket.objects.filter(user=user)

                    if basket_items.exists():
                        # Проверяем способ оплаты
                        payment_on_get = request.POST.get('payment_on_get', '0') == '1'  # '1' - оплата при получении

                        # Если оплата картой, проверяем номер карты
                        if not payment_on_get:
                            card_number = request.POST.get('card-number', '').replace(' ', '')
                            if card_number != '4242424242424242':
                                return JsonResponse(
                                    {'success': False, 'error': 'Ошибка оплаты. Проверьте данные карты.'})
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            # phone_number=form.cleaned_data['phone_number'],
                            # pharmacy=form.cleaned_data['pharmacy'],
                            # payment_on_get=form.cleaned_data['payment_on_get'],
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
                        basket_items.delete()

                        # Возвращаем успешный ответ
        #                 return JsonResponse({
        #                     'success': True,
        #                     'redirect_url': reverse('orders:order_detail', args=[order.id]),
        #                 })
        #             else:
        #                 return JsonResponse({'success': False, 'error': 'Ваша корзина пуста.'})
        #     except ValidationError as e:
        #         return JsonResponse({'success': False, 'error': str(e)})
        # else:
        #     return JsonResponse({'success': False, 'error': 'Недопустимый метод запроса.'})

                        messages.success(request, 'Заказ оформлен!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('basket:order')
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



def payment_process(request):
    # Пример суммы к оплате (можно заменить на реальную логику)
    # total_price = baskets.total_price  # Сумма в рублях
    #
    # context = {
    #     'total_price': total_price,
    # }
    # return render(request, 'orders/payment_process.html', context=context)
    return render(request, 'orders/payment_process.html')