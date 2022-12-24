from django.db import models
# from django.contrib.auth.models import User
import uuid
# Create your models here.


class Product(models.Model):
    owner = models.ForeignKey("users.Profile",on_delete=models.CASCADE,null=True,blank=True)
    fruit_name=models.CharField(max_length=200,blank=True,null=True)
    company_name=models.CharField(max_length=500,blank=True,null=True)
    location = models.CharField(max_length=500,blank=True,null=True)
    price=models.FloatField(blank=True,null=True)
    featured_image=models.ImageField(null=True,blank=True,default="default.jpg")
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
    fruits = models.ManyToManyField(Product,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    created =models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True,unique=True)
    def __str__(self):
        return str(self.name)
    



