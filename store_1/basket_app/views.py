
from django.shortcuts import get_object_or_404, redirect, render
from basket_app.models import Basket
from products_app.models import Products
from django.template.loader import render_to_string
from basket_app.utils import get_user_baskets


def basket_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user, product=product)
        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
             Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
        baskets = Basket.objects.filter(
            session_key=request.session.session_key, product=product)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.quantity += 1
                basket.save()
        else:
            Basket.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def basket_plus(request, basket_id):
    # Получаем объект корзины по id
    basket = Basket.objects.get(id=basket_id)

    # Увеличиваем количество на единицу
    basket.quantity += 1
    basket.save()

    # Перенаправляем пользователя на предыдущую страницу
    return redirect(request.META['HTTP_REFERER'])


def basket_minus(request, basket_id):
    # Получаем объект корзины по id
    basket = Basket.objects.get(id=basket_id)

    # Проверяем, не равняется ли quantity единице
    if basket.quantity > 1:
        # Уменьшаем количество на единицу
        basket.quantity -= 1
        basket.save()

    return redirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return redirect(request.META['HTTP_REFERER'])









