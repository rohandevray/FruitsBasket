from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name="products"),
    path('add-product/',views.addProduct,name="add-product"),
    path('single-fruit/<str:pk>/',views.addItem,name="single-fruit"),
    path('cart/',views.myCart,name="cart"),
    path('delete/<str:pk>/',views.deleteItem,name="delete"),
]