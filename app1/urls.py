from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePageView),
    path('signup',views.signupPageView),
    path('about',views.aboutPageView),
    path('dashboard',views.login),
    path('contact',views.contactPageView),
    path('addstudent',views.addStudentPageView),
    path('addstaff',views.addStaffPageView),
    path('showstudent',views.showStudentPageView),
    path('showstaff',views.showStaffPageView),
    path('deletestudent',views.deleteStudent),
    path('deletestaff',views.deleteStaff),
]