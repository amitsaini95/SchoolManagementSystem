from django.shortcuts import render,redirect
from .forms import SchoolForm
from .models import SchoolProfileModel
from StudentApp.models import StudentProfileModel
from StudentApp.forms import StudentProfileForm
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
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
    schoolStudent=SchoolProfileModel.objects.get(admin=request.user)
    q=request.GET.get('studentName')  if request.GET.get('studentName') != None else ''
    schoolstudentList=schoolStudent.students.filter(Q(name__icontains=q))
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
def AddStudentView(request):
    
    schoolName=SchoolProfileModel.objects.get(admin=request.user)
    if request.method =="POST":
        form=StudentProfileForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['name']
            studentUser=User.objects.create_user(username=username)
            password=username[:3]+"@123"
            studentUser.set_password(password)
            studentUser.save()
            data=form.save(commit=False)
            data.user=studentUser
            data.save()
            schoolName.students.add(data)
            schoolName.save()
       
            return redirect('SchoolApp:Dashboard')
    else:
        form=StudentProfileForm()
    context={
        'form':form
    }
    return render(request,"addstudent.html",context)
def DeleteStudentView(request,id):
    schoolstudent=StudentProfileModel.objects.get(id=id)
    schoolstudent.delete()
    return redirect('SchoolApp:StudentList')