from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from webapp.models.products import Product

# Create your models here.


class Product_in_cart(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.RESTRICT, 
        null=False,
        blank=False,
        default=1
        )
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=False,
        blank=False,
        verbose_name="Остаток"
        )
    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )

    def __str__(self):
        return f"{self.product} - {self.quantity}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()