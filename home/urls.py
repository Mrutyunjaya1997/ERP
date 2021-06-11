from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('viewcourse',views.viewcourse,name='viewcourse'),
    path('applycourse',views.applycourse,name='applycourse'),
    path('editprofile',views.editprofile,name='editprofile'),
   
]
