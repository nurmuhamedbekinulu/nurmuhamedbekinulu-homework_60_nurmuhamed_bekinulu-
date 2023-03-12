from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from webapp.models.categories import Category

# Create your models here.


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Имя товара"
        )
    description = models.TextField(
        max_length=3000,
        null=True, blank=True,
        verbose_name="Описание товара"
        )
    image = models.CharField(
        max_length=300,
        null=False, blank=False,
        verbose_name="Фото товара"
        )
    category = models.ForeignKey(
        Category,
        on_delete=models.RESTRICT, 
        null=False,
        blank=False,
        default=1
        )
    product_left = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=False,
        blank=False,
        verbose_name="Остаток"
        )
    price = models.DecimalField(
        validators=[MinValueValidator(0)],
        max_digits=7,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name="Стоимость"
        )
    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )

    def __str__(self):
        return f"{self.title} - {self.description}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()