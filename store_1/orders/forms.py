from django import forms
from pharmacy.models import Pharmacy
from orders.models import Order

class CreateOrderForm(forms.Form):
    phone_number = forms.CharField(label="Номер телефона", max_length=20)

    pharmacy = forms.ModelChoiceField(
        queryset=Pharmacy.objects.all(),
        label="Аптека для самовывоза",
        required=True,
        empty_label="-- Выберите аптеку --",
    )

    # payment_on_get = forms.ChoiceField(
    #     choices=[
    #         ("0", 'Оплата картой'),
    #         ("1", 'Оплата при получении'),
    #     ],
    #     label="Способ оплаты",
    # )

    class Meta:
        model = Order
        fields = ['phone_number', 'pharmacy']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем выбор аптеки
        self.fields['pharmacy'].queryset = Pharmacy.objects.all()

