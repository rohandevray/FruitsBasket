from django.shortcuts import render ,redirect
from .models import Product ,Cart
from .forms import ProductForm ,ItemForm
#for the authentication
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    context={'products':products}
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



@login_required(login_url='login')
def myCart(request):
    profile = request.user.profile
    fruits = Product.objects.filter(owner=profile)
    total_fruits = fruits.__len__()
    subtotal = 0
    for fruit in fruits:
        subtotal += fruit.getTotal
    context={'fruits':fruits,'total_fruits':total_fruits,'subtotal':subtotal}
    return render(request,'products/user-cart.html', context)
    

@login_required(login_url='login')
def addItem(request,pk):
    profile = request.user.profile
    product = Product.objects.get(id=pk)
    form = ItemForm(instance=product)
    if request.method == 'POST':
        form = ItemForm(request.POST,instance=product)
        if form.is_valid():
            product= form.save(commit=False)
            product.quantity = request.POST['quantity']
            product.owner = profile
            product.save()
            return redirect('products')
    context={'product':product,'form':form}
    return render(request,'products/add-item.html',context)


@login_required(login_url="login")
def deleteItem(request,pk):
    profile = request.user.profile
    product = Product.objects.filter(id=pk)
    if request.method == 'POST':
        print(product.values_list)
        print(profile)
        messages.success(request,"Item was removed successfully!")
        return redirect('cart')
    context={'profile':profile,'product':product}
    return render(request,'delete_template.html',context)
