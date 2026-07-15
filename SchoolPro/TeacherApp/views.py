from django.shortcuts import render

# Create your views here.
def TeacherDashBoardView(request):
    return render(request,"teacherDashboard.html")