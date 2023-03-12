from django import forms
from source.webapp.models.products import Product
from django.core.validators import BaseValidator


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
    title = forms.CharField(
        max_length=200,
        validators=(CustomMinLenValidator(2), CustomMaxLenValidator(200)))
    description = forms.CharField(
        max_length=3000,
        validators=(CustomMinLenValidator(2), CustomMaxLenValidator(3000)))

    class Meta:
        model = Product
        fields = {'name', 'description', 'image',
                  'category', 'product_left', 'price'}
        labels = {
            'name': 'Имя товара',
            'description': 'Описание товара',
            'image': 'Фото товара',
            'category': 'Категория',
            'product_left': 'Остаток',
            'price': 'Стоимость'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')
