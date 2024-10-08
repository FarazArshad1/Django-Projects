
from django.contrib import admin
from django.urls import path
from . import views
from . import Core_operation

urlpatterns = [
    path("",views.Home_Page,name="My_Home_Page"),
    path("Learning_Django_About_Us",views.About_Page,name = "My_About_Page"),
    path("contact_page",views.contact_page, name = "My_Contact_Page"),
    path('gallery_page',views.gallery_page,name='Gallery_Page_Here'),
    path("login_page",views.login_page,name="My_Login_Page"),
    path("Student_list",views.list_student,name="List_of_Student"),
    path('Student_merit_list',views.Student_merit_list,name="Merit_list"),
    path('Counting',views.Display_odd_even,name="Odd_Even_list"),
    path('Admission_Process',Core_operation.Admns_page,name="Core_Opeartion_page"),
    path("Find_sum_page",views.Sum_page,name="Find Sum Page"),
    path('calculate_sum',views.calculate_sum,name='result fint'),
    path('calculate_sub',views.calculate_sub,name='result sub find'),
    path('find_multi',views.Find_multi,name='Find Multiplication of two number'),
    path('student_save',views.Add_student,name='Save Student Record'),
    path('Employee_Add',views.Employee_Add,name='Employee_Add Data'),
    path('Employee_Delete',views.Employee_Delete,name='Employee_Delete'),
    path('Employee_Update',views.Employee_Update,name='Employee_Update'),
    path('Employee_Display',views.Employee_Display,name='Employee_Display'),
    path('delete_Record',views.delete_Record,name='Delete The selected Tabel Row'),
    path('update_record',views.update_record,name='Table Row Selected Update'),
    path('update_emp',views.update_emp,name="Update Employee Record"),
    path('Save_Emp_Data',views.Save_Emp_Data,name='Save Employee Record'),
    path('login',views.login, name='Login Page Access'),
    path('newuser',views.newuser, name='New User Access Page'),
    path('logout',views.logout,name='Logout Code'),
    path('Welcome_page',views.welcome,name='Jump into welcome page'),
    path('Transaction',views.Transaction,name='Transaction bank Satement'),
    path('change_password', views.change_password,name='Change Password'),
    path('Teacher_info',views.Teacher_info,name='Teacher Data')
]
