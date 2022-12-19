from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name="products"),
    path('add-product/',views.addProduct,name="add-product")
]