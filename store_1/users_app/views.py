from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from basket_app.models import Basket
from users_app.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from orders.models import Order, OrderItem

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                if session_key:
                    Basket.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main_app:index'))
    else:
        form = UserLoginForm()

    context = {

        'title': 'Авторизация',
        'form': form
    }
    return render(request, 'users_app/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Basket.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f"{user.username}, Вы зарегистрированы")
            return HttpResponseRedirect(reverse('main_app:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Регистрация',
        'form':form
    }
    return render(request, 'users_app/registration.html', context)

@login_required  #запрет для незарег. пользователей
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    orders = Order.objects.filter(user=request.user).prefetch_related( # вывод заказов клиента в профиль
        Prefetch(
            "orderitem_set",
            queryset=OrderItem.objects.select_related("product"),
        )
    ).order_by("-id")

    context = {
        'title': 'Home - Кабинет',
        'form': form,
        'orders': orders
    }
    return render(request, 'users_app/profile.html', context)

def users_basket(request):
    return render(request, 'users_app/users_basket.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main_app:index'))