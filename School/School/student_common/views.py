from django.shortcuts import render

# Create your views here.

def Home_Page(request):
    return render(request,"Home.html")

def About_Page(request):
    return render(request,"About.html")

def contact_page(request):
    return render(request,'contact.html')

def gallery_page(request):
    return render(request,"Gallery.html")

def login_page(request):
    return render(request,'Login.html')

def list_student(request):
    students = {
        "Name" : "Faraz",
        "Branch" : "BBIT",
        "Mobile" : "+9287654329"
    }

    return render(request, 'listStudent.html',students)

def Student_merit_list(request):
    merit = [12,45,435,3,4,4,646,43,54,33,544,32,53]
    return render(request, 'Merit_List.html',{"data" : merit})

def Display_odd_even(request):
    record = []
    for i in range(51):
        record.append(i)
    return render(request,"Odd_even.html",{"data":record})