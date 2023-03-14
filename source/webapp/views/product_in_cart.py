from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, CreateView, UpdateView

from webapp.models import Product, Product_in_cart
from webapp.forms import Add_in_cart_Form



class CartDetail(DeleteView):
    template_name = 'cart_detail.html'
    model = Product_in_cart



class CartCreateView(CreateView):
    template_name = 'product_in_cart_create.html'
    model = Product_in_cart
    form_class = Add_in_cart_Form

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        product_in_cart = form.save(commit=False)
        product_in_cart.product = product
        product_in_cart.save()
        return redirect('index')


