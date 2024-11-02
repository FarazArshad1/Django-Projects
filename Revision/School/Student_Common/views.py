from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, "Home.html")

def about_us_page(request):
    return render(request, 'About.html')

def contact_page(request):
    return render(request, 'Contact.html')

def gallary_page(request):
    return render(request, "Gallary.html")

def login_page(request):
    return render(request, 'Login.html')

def list_student(request):
    students = {
        "Name" : "Rohan",
        "Branch" : "CSE",
        "Mobile" : "+987654321"
    }

    return render(request, "ListStudents.html", students)