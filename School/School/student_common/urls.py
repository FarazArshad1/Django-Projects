
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
    path('Admission_Process',Core_operation.Admns_page,name="Core_Opeartion_page")
]
