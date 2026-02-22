from django.contrib import admin
from .models import Faculty, Student, Subject, Attendance, Notification

admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Notification)