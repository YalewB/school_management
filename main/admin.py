from django.contrib import admin
from .models import Course, Student, Teacher, Grade, Parent, Admin, Director, Finance, Enrollment

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Parent)
admin.site.register(Admin)
admin.site.register(Director)
admin.site.register(Finance)
admin.site.register(Enrollment)