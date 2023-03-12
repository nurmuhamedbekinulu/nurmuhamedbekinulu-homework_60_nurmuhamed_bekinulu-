from django.urls import path
from webapp.views.base import index_view
from webapp.views.products import add_view, detail_view, update_view, delete_view, confirm_delete


urlpatterns = [
    path("", index_view, name='index'),
    path("product/", index_view),
    path("product/add/", add_view, name='product_add'),
    path("product/<int:pk>", detail_view, name='product_detail'),
    path("product/<int:pk>/update/", update_view, name='product_update'),
    path("product/<int:pk>/delete/", delete_view, name='product_delete'),
    path("product/<int:pk>/confirm_delete/",
         confirm_delete, name='confirm_delete'),
]
