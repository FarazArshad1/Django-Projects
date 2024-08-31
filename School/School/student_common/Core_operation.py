from django.shortcuts import render
import datetime

def Admns_page(request):
    tm = datetime.datetime.now( )
    return render(request,"Admns.html",{'Title':"Dav",'current_time':tm})