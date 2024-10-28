from django.shortcuts import render,redirect
from .forms import UserLoginForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

# Create your views here.


def loginpage(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request,user)
        if next:
            return redirect(next)
        return ('/')
    context = {'form' : form}
    return render(request,'login.html',context)