from django.urls import path
from .import views
app_name="SchoolApp"
urlpatterns=[
    path('schoolProfile',views.SchoolProfileView,name="schoolprofile"),
    path('',views.DashboardView,name="Dashboard")
]