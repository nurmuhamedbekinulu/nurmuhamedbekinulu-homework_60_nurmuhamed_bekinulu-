from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Категория"
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время и дата создания"
        )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Время и дата обновления"
        )
    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
