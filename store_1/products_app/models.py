from django.db import models

from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Группа')

    def __str__(self):
        return f"{self.name},{self.id}"

    class Meta:

        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name

class Recipe_status(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Рецептурный статус')

    class Meta:
        verbose_name = 'Рецептурный статус'
        verbose_name_plural = 'Рецептурные статусы'

    def __str__(self):
        return self.name

class Storage_conditions(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Условия хранения')

    class Meta:
        verbose_name = 'Условия хранения'
        verbose_name_plural = 'Условия хранения'

    def __str__(self):
        return self.name

class Price_category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Ценовая категория')

    class Meta:
        verbose_name = 'Ценовая категория'
        verbose_name_plural = 'Ценовые категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название и дозировка')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Инструкция')
    image = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена базовая')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Группа')
    price_category = models.ForeignKey(to=Price_category, on_delete=models.PROTECT, verbose_name='Ценовая категория')
    storage_conditions = models.ForeignKey(to=Storage_conditions, on_delete=models.PROTECT, verbose_name='Условия хранения')
    recipe_status= models.ForeignKey(to=Recipe_status, on_delete=models.PROTECT, verbose_name='Рецептурный статус')


    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}, Количество {self.quantity}"

    def display_id(self):
        return f"{self.id:06}"

    def retail_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price