from django.shortcuts import render,redirect
from .forms import SchoolForm
from .models import SchoolProfileModel
from StudentApp.models import StudentProfileModel
from StudentApp.forms import StudentProfileForm
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
    schoolstudentCount=SchoolProfileModel.objects.get(admin=request.user).students.all().count()
    context={
        'schoolstudentCount':schoolstudentCount
    }
    
    return render(request,"dashboard.html",context)
def StudentListView(request):
    schoolstudentList=SchoolProfileModel.objects.get(admin=request.user).students.all()
    context={
        'schoolstudentList':schoolstudentList
    }
    
    return render(request,"studentList.html",context)
def StudentProfileUpdateView(request,id):
    schoolStudentInstance=StudentProfileModel.objects.get(id=id)
    if request.method =="POST":
        form=StudentProfileForm(request.POST,instance=schoolStudentInstance)
        if form.is_valid():
            form.save()
            return redirect('SchoolApp:Dashboard')
    else:
        form=StudentProfileForm(instance=schoolStudentInstance)
    context={
        'form':form
    }
   
    return render(request,"studentprofileUpdate.html",context)