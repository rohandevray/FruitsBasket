from django.shortcuts import render ,redirect
from .models import Product ,Cart
from .forms import ProductForm ,ItemForm
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



@login_required(login_url='login')
def myCart(request):
    fruits = Product.objects.filter(is_selected=True)
    total_fruits = fruits.__len__()
    subtotal = 0
    for fruit in fruits:
        subtotal += fruit.getTotal

    context={'fruits':fruits,'total_fruits':total_fruits,'subtotal':subtotal}
    return render(request,'products/user-cart.html', context)
    

@login_required(login_url='login')
def addItem(request,pk):
    product = Product.objects.get(id=pk)
    form = ItemForm(instance=product)
    if request.method == 'POST':
        form = ItemForm(request.POST,instance=product)
        if form.is_valid():
            product= form.save(commit=False)
            product.quantity = request.POST['quantity']
            if product.toggle == False:
                product.is_selected =True
            product.save()
            return redirect('products')
    context={'product':product,'form':form}
    return render(request,'products/add-item.html',context)
