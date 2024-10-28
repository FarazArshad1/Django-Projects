from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path(route ="login_teacher",view = views.login_teacher,name="Login Teacher"),
    path(route ="about_teacher", view= views.about_teacher, name = "About Teacher"),
]