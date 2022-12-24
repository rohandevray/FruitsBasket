from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Product(models.Model):
    fruit_name=models.CharField(max_length=200,blank=True,null=True)
    company_name=models.CharField(max_length=500,blank=True,null=True)
    location = models.CharField(max_length=500,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    featured_image=models.ImageField(null=True,blank=True,default="default.jpg")
    is_selected =models.BooleanField(blank=True,null=True,default=False)
    quantity = models.IntegerField(blank=True,null=True,default=0)
    created =models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    def __str__(self):
        return self.fruit_name
    
    @property
    def toggle(self):
        return self.is_selected

    @property
    def getTotal(self):
        grand = (self.price) * (self.quantity)
        return grand

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    fruits = models.ManyToManyField(Product,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    created =models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    def __str__(self):
        return str(self.name)
    



