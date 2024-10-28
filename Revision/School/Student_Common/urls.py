from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(route="",view=views.home_page,name="My Home Page"),
    path(route="about_us_page",view=views.about_us_page,name="About Us Page"),
    path(route = 'contact_page',view=views.contact_page, name = "Contact Page"),
    path(route="gallary_page", view=views.gallary_page, name= "Gallary Page"),
    path(route="login_page", view = views.login_page, name = "Login Page")
]