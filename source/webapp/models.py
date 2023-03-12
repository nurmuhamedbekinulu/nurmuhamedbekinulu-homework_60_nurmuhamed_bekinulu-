from django.db import models
from static.classes.static import Static
from django.core.validators import MinValueValidator

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, null=False,
                            blank=False, verbose_name="Имя товара")
    description = models.TextField(
        max_length=3000, null=True, blank=True, verbose_name="Описание товара")
    image = models.CharField(max_length=300, null=False, blank=False,
                             verbose_name="Фото товара")
    category = models.CharField(max_length=200, null=False, blank=False,
                                choices=Static.choices, default='other', verbose_name="Категория")
    product_left = models.IntegerField(validators=[MinValueValidator(
        0)], null=False, blank=False, verbose_name="Остаток")
    price = models.DecimalField(validators=[MinValueValidator(
        0)], max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Стоимость")

    class Meta:
        ordering = ['category', 'name']
