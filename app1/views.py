#from typing import AwaitableGenerator
from django.contrib import auth
from django.contrib.auth import logout , authenticate
from app1.models import ContactUs, Login, addStaff, addStudent
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.

def signupPageView(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        umail=request.POST['umail']
        upass=request.POST['upass']
        x=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=umail,password=upass)
        x.save()
        print("User Created Succesfullly!")
        return render(request,'app1/signup.html')

    else:
        return render(request,'app1/signup.html')

def homePageView(request):
    return render(request,'app1/index.html')

def aboutPageView(request):
    return render(request,'app1/about.html')
    

def contactPageView(request):
    if request.method=='POST':
        fname=request.POST['fname']
        umail=request.POST['umail']
        qry=request.POST['qry']
        print(fname,umail,qry)
        x=ContactUs.objects.create(full_name=fname,umail=umail,qry=qry)
        x.save()
        return render(request,'app1/contact.html')
    else:
        return render(request,'app1/contact.html')

def addStudentPageView(request):
    if request.method=='POST':
        fname=request.POST['fname']
        umail=request.POST['umail']
        contact_num=request.POST['c_number']
        course=request.POST['course']
        print(fname,umail,contact_num,course)
        x=addStudent.objects.create(full_name=fname,umail=umail,contact_num=contact_num,course=course)
        x.save()
        messages.success(request, 'Student Added Successfully')
        return render(request,'app1/add_student.html')

    else:
        return render(request,'app1/add_student.html')

def addStaffPageView(request):
    if request.method=='POST':
        fname=request.POST['fname']
        umail=request.POST['umail']
        contact_num=request.POST['c_number']
        department=request.POST['department']
        print(fname,umail,contact_num,department)
        x=addStaff.objects.create(full_name=fname,umail=umail,contact_num=contact_num,department=department)
        x.save()
        messages.success(request, 'Staff Added Successfully')
        return render(request,'app1/add_staff.html')

    else:
        return render(request,'app1/add_staff.html')

def showStudentPageView(request):
    x=addStudent.objects.all()
    print(x)
    #for i in x:
    #    print(i.full_name,i.umail,i.contact_num,i.course)
    return render(request,'app1/show_student.html',{'x':x})


def showStaffPageView(request):
    x=addStaff.objects.all()
    print(x)
    return render(request,'app1/show_staff.html',{'x':x})


#==========================Testing Mode On======================

def login(request):
    if request.method=='POST':
        student_num=addStudent.objects.all()
        student_num=len(student_num)

        staff_num=addStaff.objects.all()
        staff_num=len(staff_num)

        myDict={'student_num':student_num,'staff_num':staff_num}
        uname=request.POST['uname']
        upass=request.POST['upass']
        print(uname,upass)
        x = auth.authenticate(username=uname,password=upass)
        print(x)
        if x is None:
            return render(request,'app1/index.html')

        else:
            return render(request,'app1/Dashboard.html',myDict)

    else:
        student_num=addStudent.objects.all()
        student_num=len(student_num)

        staff_num=addStaff.objects.all()
        staff_num=len(staff_num)

        myDict={'student_num':student_num,'staff_num':staff_num}
        return render(request,'app1/dashboard.html',myDict)

def deleteStudent(request):
    if request.method=='POST':
        uid=request.POST['uid']
        obj=addStudent.objects.filter(id=uid).delete()
        print(obj)
        messages.success(request, 'Data Deleted !')
        return render(request,'app1/delete_student.html')

    else:
        return render(request,'app1/delete_student.html')

def deleteStaff(request):
    if request.method=='POST':
        uid=request.POST['uid']
        obj=addStaff.objects.filter(id=uid).delete()
        print(obj)
        messages.success(request, 'Data Deleted !')
        return render(request,'app1/delete_staff.html')

    else:
        return render(request,'app1/delete_staff.html')
