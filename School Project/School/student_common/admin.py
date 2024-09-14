from django.contrib import admin
from .models import Employee, Signup, Contact
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('Employee_name','Employee_id')

class MemberAdmin2(admin.ModelAdmin):
    list_display = ('Name','Email_id','Gender')

admin.site.register(Employee,MemberAdmin)
admin.site.register(Signup,MemberAdmin2)
admin.site.register(Contact)