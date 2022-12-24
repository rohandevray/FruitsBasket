from django.shortcuts import render ,redirect
from .forms import CustomUserCreationForm , CustomProfile
from django.contrib.auth.models import User
#for login/authenticate/logout
from django.contrib.auth import login ,authenticate ,logout
from django.contrib import messages
#for the authentication
from django.contrib.auth.decorators import login_required
# Create your views here.


def loginUser(request):
    page = "login"
    if request.method == 'POST':
        username = request.POST['username'].lower() #getting username & password by input field type name
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Error in process!')
    
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Sucessfully logged in')
            return redirect('products')
        else:
            messages.error(request,'Password or username is incorrect')
            
    context={'page':page}
    return render(request,'users/login_register.html',context)


def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower() #setting the username
            user.save()
            messages.success(request,'User is successfully registered!')
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request,"Something went wrong!")
        
    context={'form':form,'page':page}
    return render(request,'users/login_register.html',context)

def logoutUser(request):
    logout(request)
    messages.info(request,'User is successfully logged out!')
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    context={'profile':profile}
    return render(request,'users/profile.html',context)

@login_required(login_url='login')
def updateProfile(request):
    profile = request.user.profile
    form = CustomProfile(instance=profile)
    if request.method == "POST":
        form = CustomProfile(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request,"Updated!")
            return redirect('profile')
    context={'form':form}
    return render(request,'users/edit-profile.html',context)





