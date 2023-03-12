from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product
from django.http import HttpResponseNotFound
from django.urls import reverse
from static.classes.static import Static


# def add_view(request: WSGIRequest):
#     if request.method == "GET":
#         return render(request, 'product_create.html', context={'choices': Static.choices})

#     product_data = {
#         'name': request.POST.get('name'),
#         'description': request.POST.get('description'),
#         'image': request.POST.get('image'),
#         'category': request.POST.get('category'),
#         'product_left': request.POST.get('product_left'),
#         'price': request.POST.get('price')
#     }
#     product = Product.objects.create(**product_data)
#     return redirect('product_detail', pk=product.pk)

def add_view(request: WSGIRequest):
    errors = {}

    if request.method == "GET":
        return render(request, 'product_create.html', context={'choices': Static.choices})

    product_data = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description'),
        'image': request.POST.get('image'),
        'category': request.POST.get('category'),
        'product_left': request.POST.get('product_left'),
        'price': request.POST.get('price')
    }

    if not request.POST.get('name'):
        errors['name'] = 'Данное поле обязательно к заполнению'
    if not request.POST.get('product_left'):
        errors['product_left'] = 'Данное поле обязательно к заполнению'
    if not request.POST.get('price'):
        errors['price'] = 'Данное поле обязательно к заполнению'
    if errors:
        return render(request, 'product_create.html',
                      context={
                          'errors': errors
                      })
    else:
        product = Product.objects.create(**product_data)
        return redirect('product_detail', pk=product.pk)


def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    for choice in Static.choices:
        if choice[0] == product.category:
            choices_category = choice[1]
    return render(request, 'product.html', context={
        'product': product,
        'choices_category': choices_category
    })


def update_view(request, pk):
    errors = {}

    product = get_object_or_404(Product, pk=pk)
    if not request.POST.get('name'):
        errors['name'] = 'Данное поле обязательно к заполнению'
    if not request.POST.get('product_left'):
        errors['product_left'] = 'Данное поле обязательно к заполнению'
    if not request.POST.get('price'):
        errors['price'] = 'Данное поле обязательно к заполнению'

    if request.method == "POST":
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.image = request.POST.get('image')
        product.category = request.POST.get('category')
        product.product_left = request.POST.get('product_left')
        product.price = request.POST.get('price')
        if errors:
            return render(request, 'product_update.html',
                        context={
                            'product': product,
                            'errors': errors
                        })
        product.save()
        return redirect('product_detail', pk=product.pk)
    return render(request, 'product_update.html', context={'product': product, 'choices': Static.choices})


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})


def confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')
