from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request, 'Home.html')


@login_required
def Welcome_Dashboard(request):
    return render(request,'Welcome.html')