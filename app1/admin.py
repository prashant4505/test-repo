from django.contrib import admin
from app1.models import Login, ContactUs, addStaff, addStudent
from django.contrib.auth.models import Group,User

# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    list_display=['uid','umail','upass']

admin.site.register(Login,LoginAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    list_display=['full_name','umail','qry']

admin.site.register(ContactUs,ContactUsAdmin)

class addStudentAdmin(admin.ModelAdmin):
    list_display=['full_name','umail','contact_num','course']

admin.site.register(addStudent,addStudentAdmin) 

class addStaffAdmin(admin.ModelAdmin):
    list_display=['full_name','umail','contact_num','department']

admin.site.register(addStaff,addStaffAdmin) 