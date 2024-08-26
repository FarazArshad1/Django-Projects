
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.Home_Page,name="My_Home_Page"),
    path("Learning_Django_About_Us",views.About_Page,name = "My_About_Page")
]
