from django.urls import path
from .import views
app_name="TeacherApp"
urlpatterns = [
    path("", views.TeacherDashBoardView, name="Dashboard")
]
