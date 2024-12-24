from django.db import models
from django.contrib.auth.models import User
from users_app.models import User
class Pharmacy(models.Model):
    # Номер
    number = models.PositiveIntegerField(verbose_name="Номер")
    # Название (опционально)
    name = models.CharField(max_length=255, verbose_name="Название", blank=True, null=True)
    # Адрес
    address = models.CharField(max_length=255, verbose_name="Адрес")
    # Телефон
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    # Количество касс
    cash_registers = models.PositiveIntegerField(verbose_name="Количество касс")
    # Примерная товароёмкость (инт)
    capacity = models.PositiveIntegerField(verbose_name="Товароёмкость")

    # Режим работы (радиокнопка)
    WORK_MODE_CHOICES = [
        ('24/7', 'Круглосуточно'),
        ('9-18', 'С 9:00 до 18:00'),
        ('10-20', 'С 10:00 до 20:00'),
    ]
    work_mode = models.CharField(
        max_length=10,
        verbose_name="Режим работы",
        choices=WORK_MODE_CHOICES,
        default='9-18'
    )

    # Сотрудники (внешний ключ на User с условием is_staff)
    employees = models.ManyToManyField(
        User,
        verbose_name="Сотрудники",
        limit_choices_to={'is_staff': True},
        blank=True
    )

    def __str__(self):
        return f"Аптека №{self.number} ({self.address})"

    class Meta:
        verbose_name = "Аптека"
        verbose_name_plural = "Аптеки"