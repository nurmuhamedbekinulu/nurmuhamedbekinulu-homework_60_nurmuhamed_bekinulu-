from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from webapp.models.products import Product

# Create your models here.


class Order(models.Model):
    product = models.ManyToManyField(
        to='webapp.Product',
        related_name='orders',
        blank=False,
        null=False
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=False,
        blank=False,
        verbose_name="Остаток"
        )
    user_name = models.CharField(
        max_length=300,
        null=False, blank=False,
        verbose_name="Имя",
        default=1
    )
    contact = models.CharField(
        max_length=300,
        null=False, blank=False,
        verbose_name="Телефон"
    )
    address = models.CharField(
        max_length=300,
        null=False, blank=False,
        verbose_name="Телефон"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")

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
