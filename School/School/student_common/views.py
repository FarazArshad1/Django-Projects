from django.shortcuts import render
from . Mydatabase_connect import database_Connect
from .models import Employee, Signup

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


def Sum_page(request):
    return render(request,'Sum.html')

def calculate_sum(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    c = int(a) + int(b)
    return render(request,'Sum.html',{'sum': 'Result is ' + str(c)})


def calculate_sub(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = int(a) - int(b)
    return render(request,'Sum.html',{'sub': 'Result is ' + str(c)})

def Find_multi(request):
    if request.method == 'GET':
        return render(request,'Multiply.html')
    else:
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = int(a) * int(b)
        return render(request,'Multiply.html',{'sum' : 'Result is ' + str(c)})
    
def Add_student(request):
    if request.method == 'GET':
        return render(request,'Student_information.html')
    else:
        try:
           name = request.POST.get('a')
           roll = request.POST.get('b')
           branch = request.POST.get('branch')
           mydb = database_Connect()
           mycursor = mydb.cursor()
           sql = 'insert into student(student_name,roll,branch)values(%s,%s,%s)'
           value=(name,roll,branch)
           mycursor.execute(sql,value)
           mydb.commit()
           return render(request, 'Student_information.html',{'Result' : 'Record Inserted'})
        except Exception as ex:
            return render(request, 'Student_information.html',{'Result' : ex})
        

def Employee_Add(request):
    if request.method == 'GET':
        return render(request,'Employee.html')
    else:
        name = request.POST.get('empname')
        empid = request.POST.get('empid')
        department = request.POST.get('dept')
        obj = Employee(Employee_name=name, Employee_id=empid, Employee_Department=department)
        obj.save()

        return render(request,'Employee.html', {'result' : 'Data Save Sucessfully'})
    
def Employee_Delete(request):
    if request.method == 'GET':
        return render(request,'Employee_delete.html')
    else:
        try:
            emp_sno = request.POST.get('sno')
            obj = Employee.objects.get(sno=emp_sno)
            obj.delete()

            return render(request,'Employee_delete.html',{'result':'Record Deleted'})
        except:
            return render(request,'Employee_delete.html',{'result':'This Recod Does not Exist'})
        
def Employee_Update(request):
    if request.method == 'GET':
        return render(request,'Employee_Update.html')
    else:
        try:
            Empsno = request.POST.get('sno')
            name = request.POST.get('empname')
            empid = request.POST.get('empid')
            department = request.POST.get('dept')
            obj = Employee.objects.get(sno=Empsno)
            obj.Employee_name = name
            obj.Employee_id = empid
            obj.Employee_Department = department
            obj.save()
            return render(request,'Employee_Update.html',{'result': 'Data Upadte Sucessful'})
        except:
            return render(request,'Employee_Update.html',{'result': 'This record Dose Not Exsit'})
        

def Employee_Display(request):
    obj= Employee.objects.all()
    return render(request,'Employee_Display.html',{'Record' : obj})

def delete_Record(request):
    emp_sno = request.GET.get('empid')
    Employee.objects.get(sno=emp_sno).delete()
    obj = Employee.objects.all()
    return render(request,'Employee_Display.html',{'Record':obj, 'Message': emp_sno +' Record Deleted' })

def update_record(request):
    emp_sno = request.GET.get('empid')
    obj=Employee.objects.filter(sno=emp_sno).values()
    return render(request,'Update_Emp.html',{'Record' : obj[0]})

def update_emp(request):
    sn = request.POST.get('sno')
    emp_n = request.POST.get('empname')
    emp_id = request.POST.get('empid')
    emp_dept = request.POST.get('dept')
    obj = Employee.objects.get(sno = sn)
    obj.Employee_name = emp_n
    obj.Employee_id = emp_id
    obj.Employee_Department = emp_dept
    obj.save()

    obj = Employee.objects.all()
    return render(request, 'Employee_Display.html', {'Record': obj, 'Message' : 'Selected Record Updated'})

def Save_Emp_Data(request):
    emp_n = request.POST.get('empname')
    emp_id = request.POST.get('empid')
    emp_dept = request.POST.get('empdpt')
    obj = Employee(Employee_name = emp_n, Employee_id = emp_id, Employee_Department = emp_dept)
    obj.save()
    obj = Employee.objects.all()
    return render(request,'Employee_Display.html',{'Record':obj,'Message':emp_n + ' Record Inserted'})


def newuser(request):
    if request.method == 'GET':
        return render(request, 'Newuser.html')
    else:
        try:
            name = request.POST.get('nm')
            email = request.POST.get('em')
            password = request.POST.get('ps')
            gender = request.POST.get('gender')
            state = request.POST.get('st')
            mobile = request.POST.get('mobile')
            obj = Signup(Name = name, Email_id = email, Password = password, Gender = gender, State = state, Mobile = mobile)
            obj.save() # Saving all the above objects in database
            return render(request, 'Logs.html' ,{'message' : 'Done'})
        except Exception as ex:
            return render(request, 'Newuser.html', {'message' : ex})
        

def login(request):
    if request.method == 'GET':
        return render(request,'Logs.html')
    else:
        try:
            email = request.POST.get('em')
            password = request.POST.get('psw')
            obj = Signup.objects.filter(Email_id = email, Password = password).values()
            if(len(obj)>0):
                return render(request,'Welcome.html')
            else:
                return render(request,'Logs.html',{'message2' : 'Incorrect Email or Password'})
        except Exception as ex:
            return render(request, 'Logs.html' ,{'message2' : ex})
