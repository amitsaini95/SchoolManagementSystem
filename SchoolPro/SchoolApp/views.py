from django.shortcuts import render,redirect
from .forms import SchoolForm
from .models import SchoolProfileModel
# Create your views here.
def SchoolProfileView(request):
    schoolInstance=SchoolProfileModel.objects.get(admin=request.user)
    if request.method =="POST":
        form=SchoolForm(request.POST,instance=schoolInstance)
        if form.is_valid():
            form.save()
            return redirect('SchoolApp:Dashboard')
    else:
        form=SchoolForm(instance=schoolInstance)
    context={
        'form':form
    }
    return render(request,"schoolprofile.html",context)
def DashboardView(request):
    return render(request,"dashboard.html")