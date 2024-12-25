from django.shortcuts import render
from pharmacy.models import Pharmacy

def index(request):


    context: dict = {
        'title': 'Главная страница магазина Аптека (V)(Это учебный сайт)',
        'content': 'Аптека (V)(Это учебный сайт)',

    }
    return render(request, 'main_app/index.html', context)

def about(request):
    # Получаем список всех аптек
    pharmacies = Pharmacy.objects.all()

    context: dict = {
        'title': 'О нас',
        'content_page': 'Адрес. Телефон.(Это учебный сайт)',
        'text1': 'Наши преимущества'   ,
        'text2': 'Адрес. Телефон.(Это учебный сайт)',
        'pharmacies': pharmacies,  # Добавляем список аптек в контекст
    }
    return render(request, 'main_app/about.html', context)