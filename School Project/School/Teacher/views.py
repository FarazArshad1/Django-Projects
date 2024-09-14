from django.shortcuts import render

# Create your views here.

def Teacher_Login(request):
    return render(request,'Teacherlogin.html')

def About_Page(request):
    return render(request, 'AboutTeacher.html')