from django.urls import path
from .import views
app_name="BaseApp"
urlpatterns=[
    path('',views.HomeView,name="Home"),
    path('login',views.LoginView,name="Login"),
    path('showSignList',views.showsignbuttonList,name="showsignbuttonList"),
    path('schoolSignUp',views.schoolSignUpView,name="SchoolSignUp"),
    path('Logout',views.LogoutView,name="Logout"),
    path('Send_otp',views.SendOTPView,name="SendOtp")


]