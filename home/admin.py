from django.contrib import admin
from . models import courses, ExtraStudentDetails, Appliedcourses


# Register your models here.

admin.site.register(courses)
admin.site.register(ExtraStudentDetails)
admin.site.register(Appliedcourses)

