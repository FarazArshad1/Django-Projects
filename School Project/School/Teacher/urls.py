
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("Login_Teacher",views.Teacher_Login,name="Teacher_Login_Page"),
    path("About_Teacher",views.About_Page, name = "About Teacher Page")
]
