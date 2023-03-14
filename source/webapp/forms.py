from django import forms
from webapp.models import Product, Product_in_cart, Order
from django.core.validators import BaseValidator, MinValueValidator


class CustomMaxLenValidator(BaseValidator):
    def __init__(self, limit_value):
        message = 'Максимальная длина поля %(limit_value)s. Выввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value > limit_value

    def clean(self, value):
        return len(value)


class CustomMinLenValidator(BaseValidator):
    def __init__(self, limit_value):
        message = 'Минимальная длина поля %(limit_value)s. Выввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return value < limit_value

    def clean(self, value):
        return len(value)


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        max_length=200,
        label='Имя товара',
        validators=(CustomMinLenValidator(2), CustomMaxLenValidator(200))
    )
    description = forms.CharField(
        max_length=3000,
        label='Описание товара',
        validators=(CustomMinLenValidator(2), CustomMaxLenValidator(3000))
    )
    product_left = forms.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        model = Product
        fields = ['name', 'description', 'image',
                  'category', 'product_left', 'price']
        labels = {
            'name': 'Имя товара',
            'description': 'Описание товара',
            'image': 'Фото товара',
            'category': 'Категория',
            'product_left': 'Остаток',
            'price': 'Стоимость'
        }


class Add_in_cart_Form(forms.ModelForm):
    quantity = forms.IntegerField(
        label='Количество',
        validators=[MinValueValidator(0)]
        )

    class Meta:
        model = Product_in_cart
        fields = ['quantity',]
        labels = {
            'quantity': 'Количество',
        }


class OrderForm(forms.ModelForm):
    user_name = forms.CharField(
        max_length=200,
        label='Имя',
        validators=(CustomMinLenValidator(2), CustomMaxLenValidator(200))
    )
    class Meta:
        model = Order
        fields = ['user_name', 'contact', 'address']
        labels = {
            'user_name': 'Имя пользователя',
            'contact': 'Телефон',
            'address': 'Адрес',
        }

class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')
