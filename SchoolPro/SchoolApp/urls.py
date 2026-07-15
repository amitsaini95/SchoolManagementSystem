from django.urls import path
from .import views
app_name="SchoolApp"
urlpatterns=[
    path('schoolProfile',views.SchoolProfileView,name="schoolprofile"),
    path('',views.DashboardView,name="Dashboard"),
    path('studentList',views.StudentListView,name="StudentList"),
    path('StudentProfileUpdate/<int:id>',views.StudentProfileUpdateView,name="StudentProfileUpdate"),
    path('addStudent',views.AddStudentView,name="AddStudent"),
    path('deleteStudent/<int:id>',views.DeleteStudentView,name="DeleteStudent"),
    path('TeacherList',views.TeacherListView,name="TeacherList"),
    path('addTeacher',views.AddTeacherView,name="AddTeacher"),
    path('bulkuploadStudent',views.BulkuploadStudentView,name="BulkuploadStudent"),
    path('Showbulkstudentlist',views.ShowbulkstudentlistView,name="ShowbulkstudentList"),
    path('studentListbulk',views.studentListbulkView,name="StudentListbulk"),
    path('courseSelect',views.CourseSelectView,name="CourseSelectOption"),
    path('generate_pdf',views.generatePDFView,name="generatePdf")
    
]