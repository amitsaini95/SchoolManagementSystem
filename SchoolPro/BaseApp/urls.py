from django.urls import path
from .import views
urlpatterns=[
    path('',views.HomeView,name="Home"),
    path('login',views.LoginView,name="Login"),
    path('dashboard',views.DashboardView,name="Dashboard")
]