from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Product
from static.classes.static import Static


def index_view(request: WSGIRequest):
    products = Product.objects.filter(product_left__gte=1)
    context = {
        'products': products,
        'choices': Static.choices
    }
    return render(request, 'index.html', context=context)
