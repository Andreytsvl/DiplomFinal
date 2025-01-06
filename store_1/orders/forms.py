from django import forms
from pharmacy.models import Pharmacy

class CreateOrderForm(forms.Form):
    phone_number = forms.CharField(label="Номер телефона", max_length=20)

    pharmacy = forms.ModelChoiceField(
        queryset=Pharmacy.objects.all(),
        label="Аптека для самовывоза",
        required=True,
        empty_label="-- Выберите аптеку --",
    )

    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'Оплата картой'),
            ("1", 'Оплата при получении'),
        ],
        label="Способ оплаты",
    )


