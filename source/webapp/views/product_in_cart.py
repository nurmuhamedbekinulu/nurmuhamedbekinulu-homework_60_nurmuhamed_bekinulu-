from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, CreateView, UpdateView, ListView

from webapp.models import Product, Product_in_cart
from webapp.forms import Add_in_cart_Form

from django.db.models import F, Sum, ExpressionWrapper, IntegerField


class CartCreateView(CreateView):
    template_name = 'product_in_cart_create.html'
    model = Product_in_cart
    form_class = Add_in_cart_Form

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        product_in_cart = form.save(commit=False)
        product_in_cart.product = product
        quantity = product_in_cart.quantity
        if quantity <= product.product_left:
            product_in_cart.save()
            return redirect('index')
        else:
            form.add_error('quantity', 'На складе не достаточно товара, введите число не выше остатка')
            return self.form_invalid(form)


class CartDetail(ListView):
    template_name = 'cart_detail.html'
    context_object_name = 'product_in_cart'
    model = Product_in_cart
    paginate_by = 10
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_per_item = Product_in_cart.objects.annotate(
            total_per_item=ExpressionWrapper(
                F('product__price') * F('quantity'), output_field=IntegerField())
        ).values('id', 'total_per_item')
        total_per_item_dict = {
            item['id']: item['total_per_item'] for item in total_per_item}
        context['total_per_item'] = total_per_item_dict
        context['overall_total'] = Product_in_cart.objects.aggregate(
            overall_total=Sum(ExpressionWrapper(
                F('product__price') * F('quantity'), output_field=IntegerField()))
        )['overall_total'] or 0

        return context
