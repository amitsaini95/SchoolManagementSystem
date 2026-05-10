from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth  import authenticate, login,logout 
# Create your views here.
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
        
                return redirect('Dashboard')
    else:   
            form=LoginForm()
    return  render(request,'login.html',{'form':form})

