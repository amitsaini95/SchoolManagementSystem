from django.urls import path
from .import views
app_name="BaseApp"
urlpatterns=[
    path('',views.HomeView,name="Home"),
    path('login',views.LoginView,name="Login"),
    path('showSignList',views.showsignbuttonList,name="showsignbuttonList"),
    path('schoolSignUp',views.schoolSignUpView,name="SchoolSignUp"),
<<<<<<< HEAD
    path('studentSignUp',views.studentSignUpView,name="StudentSignUp"),
    path('Logout',views.LogoutView,name="Logout")
=======
    path('studentSignUp',views.studentSignUpView,name="StudentSignUp")
>>>>>>> b2c084602b28acf29cfc940bb484ffbadc2d8282

]