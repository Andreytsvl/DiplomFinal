from django.contrib import admin
from basket_app.models import Basket

# admin.site.register(Basket)

class BasketTabAdmin(admin.TabularInline): # отображение корзины в карточке пользователя
    model = Basket
    fields = "product", "quantity", "created_timestamp"
    search_fields = "product", "quantity", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1 #добавление в заказ

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["user_display", "product_display", "quantity", "created_timestamp",]
    list_filter = ["created_timestamp", "user", "product__name",]# __ чтоб не обращаться по str-методу

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    def product_display(self, obj): #переопределение отображения, см. выше
        return str(obj.product.name)