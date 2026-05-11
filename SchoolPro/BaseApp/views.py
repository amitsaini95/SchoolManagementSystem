from django.shortcuts import render,redirect
from .forms import LoginForm
from SchoolApp.forms import SchoolForm
from django.contrib.auth  import authenticate, login,logout 
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
def HomeView(request):
    return render(request,"base.html")
def LoginView(request):
    if request.method == "POST":
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username'] 
            upass = form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is  not None: 
                login(request,user)
        
                return redirect('SchoolApp:Dashboard')
    else:   
            form=LoginForm()
    return  render(request,'login.html',{'form':form})

def showsignbuttonList(request):
    return render(request,"showsignbuttonList.html")
def schoolSignUpView(request):
    print("school")
    if request.method == "POST":
        form=SchoolForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['name']
            user=User.objects.create_user(username=username)
            user.set_password(username[:3]+"@123")
            user.save()
            data=form.save(commit=False)
            data.admin=user
            data.save()
            return redirect('BaseApp:Login')
    else:
        form=SchoolForm()
    return render(request,"schoolSignup.html",context={'form':form})