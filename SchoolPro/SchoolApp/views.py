from django.shortcuts import render,redirect,HttpResponse
from django.core import serializers
from django.http import JsonResponse
from .forms import SchoolForm
from .models import SchoolProfileModel
from StudentApp.models import StudentProfileModel,CourseModel
from .forms import *
from BaseApp.models import User
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
import json
import threading
from django.core.serializers import serialize
import csv
from django.contrib.auth.hashers import make_password
import pandas as pd
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
    schoolteacherCount=SchoolProfileModel.objects.get(admin=request.user).teachers.all().count()
    context={
        'schoolstudentCount':schoolstudentCount,
        'schoolteacherCount':schoolteacherCount
    }
    return render(request,"dashboard.html",context)
def StudentListView(request):
    schoolStudent=SchoolProfileModel.objects.get(admin=request.user)
    q=request.GET.get('studentName')  if request.GET.get('studentName') != None else ''
    schoolstudentList=schoolStudent.students.filter(Q(name__icontains=q) | Q(email__icontains=q))
    context={
            'schoolstudentList':schoolstudentList
    }
    return render(request,"studentList.html",context)
def StudentProfileUpdateView(request,id):
    schoolStudentInstance=StudentProfileModel.objects.get(id=id)
    if request.method =="POST":
        form=AddStudentSchoolForm(request.POST,instance=schoolStudentInstance)
        if form.is_valid():
            username=form.cleaned_data['name']
            password=username[:3]+"@123"
            userprofile=User.objects.get(username=schoolStudentInstance.user)
            userprofile.username=username
            userprofile.set_password(password)
            userprofile.save()
            data=form.save(commit=False)
            data.user=userprofile
            data.save()
            return redirect('SchoolApp:Dashboard')
    else:
        form=AddStudentSchoolForm(instance=schoolStudentInstance)
    context={
        'form':form
    }
    return render(request,"studentprofileUpdate.html",context)
def AddStudentView(request):
  
    schoolName=SchoolProfileModel.objects.get(admin=request.user)

    if request.method =="POST":
        Coursedata=CourseModel.objects.get(id=request.POST.get('courses'))

        stuName=request.POST.get('name')
        user=User.objects.create(username=stuName,userType="student")
        user.set_password(stuName[:3]+"@123")
        user.save()
        StudentProfileModel.objects.create(user=user,name=request.POST.get('name'),age=request.POST.get('age'),
        gender=request.POST.get('gender'),stuclass=request.POST.get('stuclass'),courses=Coursedata,
        phoneNo=request.POST.get('phoneNo'),email=request.POST.get('email'),schoolName=schoolName
        )
  
    form=AddStudentSchoolForm()
    
    context={'form':form}
    return render(request,"addstudent.html",context)
def DeleteStudentView(request,id):
    schoolstudent=StudentProfileModel.objects.get(id=id)
    user=User.objects.get(id=schoolstudent.user.id)
    schoolstudent.delete()
    user.delete()
    return redirect('SchoolApp:StudentList')
def TeacherListView(request):

    return render(request,"TeacherList.html")

def AddTeacherView(request):
    if request.method == "POST":
        form=AddSchoolTeacherForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['name']
            TeacherUser=User.objects.create_user(username=username,userType="teacher")
            password=username[:3]+"@123"
            TeacherUser.set_password(password)
            TeacherUser.save()
            data=form.save(commit=False)
            data.user=TeacherUser
            data.save()
            return redirect('SchoolApp:TeacherList')
    else:
        form=AddSchoolTeacherForm()
    context={
        'form':form
    }
    return render(request,"addteacher.html",context)

def BulkuploadStudentView(request):
    if request.method == 'POST':
        if 'uploadStudentBuk' in request.FILES:
            request.FILES.get('uploadStudentBuk')
    return render(request,"bulkUploadStudent.html")

def ShowbulkstudentlistView(request):

    searchWord = request.POST.get('uploadStudentBuk','')
    print(searchWord)
    if request.method =="POST" and request.FILES.get('uploadStudentBuk'):
        file=request.FILES.get('uploadStudentBuk')
        if file is not None:
            df = pd.read_csv(file)
            data = df.to_dict(orient='records')
            return render(request,"Showbulkstudentlist.html",context={'data':data})
    return redirect('SchoolApp:Dashboard')
 
def studentListbulkView(request):
    schoolName=SchoolProfileModel.objects.get(admin=request.user)
    studentList=[]
    if request.method == 'POST':
        studentData=json.loads(request.body)
        user_instaces=[
            User(
                username=data["name"],
                userType="student",
                password=make_password(data['name'][:3]+"@123")
            )for data in studentData]
        User.objects.bulk_create(user_instaces)
        studentList=[StudentProfileModel(**item,schoolName=schoolName,user=User.objects.get(username=item['name'])) for item in studentData]
        studata=StudentProfileModel.objects.bulk_create(studentList)
        for stu in studata:
            schoolName.students.set(studata)
            schoolName.save()

        return redirect('SchoolApp:Dashboard')
    return HttpResponse("dskf")

def CourseSelectView(request):

    data=json.loads(request.body)
    course=CourseModel.objects.filter(studentClass=data).values('id','name')
    return JsonResponse(list(course),safe=False)
