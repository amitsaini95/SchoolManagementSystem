from django.shortcuts import render

# Create your views here.
def StudentDashboardView(request):
    return render(request,"studentDashboard.html")