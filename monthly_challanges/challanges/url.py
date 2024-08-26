from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path("<int:month>", views.monthly_challange_by_number),
    path("<str:month>", views.monthly_challanges),
    path("<int:pageNo>",views.pages)
]