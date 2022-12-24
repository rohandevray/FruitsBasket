from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('profile/',views.profile,name="profile"),
    path('update-profile/',views.updateProfile,name="update-profile")
]