from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(StudentProfileModel)
admin.site.register(SubjectModel)
admin.site.register(SessionModel)
admin.site.register(CourseModel)
admin.site.register(AttendanceSubjectModel)
admin.site.register(AttendanceReport)






