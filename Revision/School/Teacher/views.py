from django.shortcuts import render

# Create your views here.

def login_teacher(request):
    return render(request, 'TeacherLogin.html')

def about_teacher(request):
    return render(request, 'AboutTeacher.html')