from django.contrib import admin
from users_app.models import User
from basket_app.admin import BasketTabAdmin
from orders.admin import OrderTabulareAdmin

#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email",]
    search_fields = ["username", "first_name", "last_name", "email",]



    inlines = [BasketTabAdmin, OrderTabulareAdmin] # отображение корзины в карточке пользователя
