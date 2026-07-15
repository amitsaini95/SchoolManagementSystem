from django.shortcuts import render,redirect,HttpResponse
from django.core import serializers
from django.http import JsonResponse
from .forms import SchoolForm
from .models import SchoolProfileModel
from StudentApp.models import StudentProfileModel,CourseModel
from .forms import *
from BaseApp.models import User
from django.db.models import Q
# Create your views here.
import json
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
import csv
from django.contrib.auth.hashers import make_password
import pandas as pd
import threading
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def generatePDFView(request):
 # 1. Initialize a byte stream buffer
    buffer = io.BytesIO()
    
    # 2. Setup the Document
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []
    
    # 3. Retrieve your QuerySet data
    # Tip: Optimize your query with select_related / prefetch_related if needed
    StudentListData = StudentProfileModel.objects.all()
    
    # 4. Construct table data grid (Header row + Data rows)
    table_data = [['ID', 'Name', 'Age','gender','email','phoneNo','SchoolName']] # Columns layout
    for counter, student in enumerate(StudentListData, start=1):
        table_data.append([
            str(counter),
            str(student.name),
            str(student.age),
            str(student.gender),
            str(student.email),
            str(student.phoneNo),
            str(student.schoolName)
           
        ])
        
    # 5. Build and Style the ReportLab Table
    pdf_table = Table(table_data)
    pdf_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a365d')), # Navy Header
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f7fafc')), # Row background
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')), # Grid lines
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    # 6. Add elements to layout story and render
    story.append(pdf_table)
    doc.build(story)
    
    # 7. Reset buffer pointer and return file
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='studentList.pdf')
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
        Coursedata=None
        try:
            Coursedata=CourseModel.objects.get(id=request.POST.get('courses'))
        except:
            pass
        stuName=request.POST.get('name')
        user=User.objects.create(username=stuName,userType="student")
        user.set_password(stuName[:3]+"@123")
        user.save()
        StudentProfileModel.objects.create(user=user,name=request.POST.get('name'),age=request.POST.get('age'),
        gender=request.POST.get('gender'),stuclass=request.POST.get('stuclass'),courses=Coursedata,
        phoneNo=request.POST.get('phoneNo'),email=request.POST.get('email'),schoolName=schoolName
        )
        student=StudentProfileModel.objects.filter(schoolName=schoolName)
        for stu in student:
            schoolName.students.add(stu)
            schoolName.save()
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
    schoolName=SchoolProfileModel.objects.get(admin=request.user)
    teacherList=TeacherProfileModel.objects.filter(newSchoolName=schoolName)
    context={'schoolTeacherList':teacherList}
    return render(request,"TeacherList.html",context)

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
    schoolName=SchoolProfileModel.objects.get(admin=request.user)
    searchWord = request.POST.get('uploadStudentBuk','')
    print(searchWord)
    if request.method =="POST" and request.FILES.get('uploadStudentBuk'):
        file=request.FILES.get('uploadStudentBuk')
        if file is not None:
            df = pd.read_csv(file)
            data = df.to_dict(orient='records')
            return render(request,"Showbulkstudentlist.html",context={'data':data,'schoolName':schoolName})
    return redirect('SchoolApp:Dashboard')
 
def studentListbulkView(request):
    studentList=[]
    schoolName=SchoolProfileModel.objects.get(admin=request.user)
    if request.method == 'POST':
        studentData=json.loads(request.body)
        
      
        for data in studentData:

            User.objects.create_user(username=data['name'],password=data['name'],userType="student")
        studentList=[StudentProfileModel(**item,schoolName=schoolName,user=User.objects.get(username=item['name'])) for item in studentData]
        studata=StudentProfileModel.objects.bulk_create(studentList)
        student=StudentProfileModel.objects.filter(schoolName=schoolName)
        for stu in student:
            schoolName.students.add(stu)
            schoolName.save()

      

       
    return HttpResponse("dskf")

 


def CourseSelectView(request):

    data=json.loads(request.body)
    course=CourseModel.objects.filter(studentClass=data).values('id','name')
    return JsonResponse(list(course),safe=False)
