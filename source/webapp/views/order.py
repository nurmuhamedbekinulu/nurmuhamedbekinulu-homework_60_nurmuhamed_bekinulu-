from django.urls import reverse_lazy
from django.views.generic import CreateView

from webapp.models import Order
from webapp.forms import OrderForm


class OrderCreateView(CreateView):
    pass
