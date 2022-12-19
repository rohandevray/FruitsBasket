from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['fruit_name','price','featured_image']
        labels = {
            'fruit_name':'Fruit',
            'price':'Price',
            'featured_image':'Image',
        }

    
class ItemForm(ModelForm):
    class Meta:
        model = Product
        fields = ['quantity']