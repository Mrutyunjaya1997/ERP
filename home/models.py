from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class courses(models.Model):
    course_name = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    offline = models.BooleanField()
    online = models.BooleanField()
    def __str__(self):
        return self.course_name+" "+self.duration

class ExtraStudentDetails(models.Model):
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=12)
    adhar = models.CharField(max_length=12)
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.student.username + ' '+ self.student.email

class Appliedcourses(models.Model):
    apply_course = models.ManyToManyField(courses)
    apply_student = models.CharField(max_length=50)
    offline = models.BooleanField()
    online = models.BooleanField()
    apply_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.apply_student
    


