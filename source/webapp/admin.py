from django.contrib import admin
from source.webapp.models.products import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'product_left', 'price')
    list_filter = ('name', 'category', 'price')
    search_fields = ('name', 'category', 'price')
    fields = ('name', 'description', 'category', 'product_left', 'price')
    readonly_fields = ('id', 'id')


admin.site.register(Product, ProductAdmin)

