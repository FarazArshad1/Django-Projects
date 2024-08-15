from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path("<int:year>", views.yearly_challenge),
    path("<str:month>", views.monthly_challenges),
]