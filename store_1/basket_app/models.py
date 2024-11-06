from django.db import models
from products_app.models import Products
from users_app.models import User


class BasketQueryset(models.QuerySet):

     def total_price(self):
         return round(sum(basket.products_price() for basket in self),2) #генератор

     def total_quantity(self):
         if self:
             return sum(basket.quantity for basket in self)
         return 0



class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'basket'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
        ordering = ("id",)

    objects = BasketQueryset().as_manager()# расширяет к-во доступных методов

    def products_price(self):
        return round(self.product.retail_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'

        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'