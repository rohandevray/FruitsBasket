from django.shortcuts import render ,redirect
from .models import Product
from .forms import ProductForm
#for the authentication
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    current_list = Product.objects.filter(is_selected=True)
    context={'products':products,'current_list':current_list}
    return render(request,'products/products.html',context)

@login_required(login_url="login")
def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("products")
     
        
            
    context={'form':form}
    return render(request,"products/product-form.html",context)