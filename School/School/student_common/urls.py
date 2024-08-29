
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home_Page,name="My_Home_Page"),
    path("Learning_Django_About_Us",views.About_Page,name = "My_About_Page"),
    path("contact_page",views.contact_page, name = "My_Contact_Page"),
    path('gallery_page',views.gallery_page,name='Gallery_Page_Here'),
    path("login_page",views.login_page,name="My_Login_Page")

]
