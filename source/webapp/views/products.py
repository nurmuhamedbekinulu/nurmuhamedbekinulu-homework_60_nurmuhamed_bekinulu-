from webapp.models import Product
from webapp.forms import ProductForm
from django.views.generic import DeleteView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy


class ProductCreateView(CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDetail(DeleteView):
    template_name = 'product.html'
    model = Product


class ProductUpdateView(UpdateView):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')
