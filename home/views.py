from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from . models import courses,ExtraStudentDetails,Appliedcourses
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'index.html')

def enquiry(request):  
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['pswd']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        student = ExtraStudentDetails()
        student.city = request.POST['city']
        student.gender = request.POST['gender']
        student.mobile = request.POST['mobile']
        student.adhar = request.POST['adhar']
        student.student = user
        student.save()
        return redirect('/')          
    else:
        return render(request, 'enquiry.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['name']
        password = request.POST['pwd']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')
    else:
        messages.info(request,'invalid credentials')
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def viewcourse(request):
    course = courses.objects.all()
    return render(request,'viewcourse.html',{'course':course})

def applycourse(request):
    if request.method == 'POST':
        c = Appliedcourses()
        c.apply_student = request.POST['username']
        c.offline = request.POST['offline']
        c.online = request.POST['online']
        c.apply_date = datetime.datetime.now()       
        c.save()
        c_name=request.POST.getlist('course')
        for i in c_name:
            cr = courses.objects.filter(id = int(i)).get()
            c.apply_course.add(cr)
        return redirect('/')

    else:
        course = courses.objects.all()
        return render(request, 'applycourses.html',{'course':course})

def editprofile(request):
    if request.method == 'POST':
        id = request.POST['u_id']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pswd']
        repassword = request.POST['repswd']
        city = request.POST['city']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        adhar = request.POST['adhar']
        u = User.objects.filter(id = id).get()
        if password != repassword:
            messages.info(request,'Password is not matching')
            return redirect('editprofile')
        else:
            u.username = username
            u.email = email
            u.set_password(password)
            u.save()
            s = ExtraStudentDetails.objects.filter(student_id = u.id).get()
            s.city = city
            s.gender = gender
            s.mobile = mobile
            s.gender = gender
            s.student = u
            s.save()
            return redirect('/')
    else:
        student = ExtraStudentDetails.objects.all()
        return render(request, 'editprofile.html',{'student':student})
        
    
    
    

    