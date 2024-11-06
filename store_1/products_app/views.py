from django.shortcuts import render, get_list_or_404

from django.core.paginator import Paginator
from products_app.models import Products
from products_app.utils import q_search


def catalog(request, category_id=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_id == 1:
        products_app = Products.objects.all()
    elif query:
        products_app = q_search(query)
    else:
        products_app = get_list_or_404(Products.objects.filter(category__id=category_id)) #ORM -запрос

    if on_sale:
        products_app = products_app.filter(discount__gt=0)
    if order_by and order_by !="default":
        products_app = products_app.order_by(order_by)

    paginator = Paginator(products_app, 3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "products_app": current_page,
        "id_url":category_id,

    }
    return render(request, "products_app/catalog.html", context)


def products(request, product_slug=False, product_id=False):
    if product_id:
        product = Products.objects.get(id=product_id) #ORM

    else:
        product = Products.objects.get(slug=product_slug)
    context = {"product": product}

    return render(request, "products_app/products.html", context=context)



