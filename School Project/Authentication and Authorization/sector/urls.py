from django.urls import path
from . import views


urlpatterns = [
    path("",views.homepage,name="Home Page"),
    path('dashboard', views.Welcome_Dashboard,name='Welcome Dashboard')
]