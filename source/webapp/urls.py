from django.urls import path
from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.products import ProductDetail, ProductUpdateView, ProductDeleteView, ProductCreateView
from webapp.views.product_in_cart import CartCreateView, CartDetail


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("product/", IndexRedirectView.as_view(), name='task_index_redirect'),
    path("product/add/", ProductCreateView.as_view(), name='product_add'),
    path("product/<int:pk>", ProductDetail.as_view(), name='product_detail'),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name='product_update'),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name='product_delete'),
    path("product/<int:pk>/confirm_delete/", ProductDeleteView.as_view(), name='confirm_delete'),
    path("cart/add/<int:pk>/", CartCreateView.as_view(), name='cart_add'),
    path("cart/", CartDetail.as_view(), name='cart_detail'),
]
