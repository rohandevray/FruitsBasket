from django.urls import path
from . import views

urlpatterns = [
    path('cart/',views.myCart,name="cart"),
    path('add-item/<str:pk>/',views.addItem,name="add-item"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('profile/',views.profile,name="profile"),
    path('update-profile/',views.updateProfile,name="update-profile")
]