from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here
monthly_challanges_list = {
    "january" : "Take bath daily in january",
    "feburary" : " Don't born or die on 29th of Feburary",
    "march" : "March Twoards your goals",
    "april" : "Jokes on you, april",
    "may" : "May i come in",
    "june" : "In June i love moon",
    "july" : "Say bye bye to july",
    "august" : "Don't rest in august",
    "september" : "Count the numbers in september",
    "october" : "Attack the neighbour in october",
    "november" : "Work hard in november",
    "december" : "Are you a lumber? December"
}

def monthly_challange_by_number(request, month):
    months = list(monthly_challanges_list.keys())
    redirected_month = months[month]
    return HttpResponseRedirect("/challanges/" + redirected_month)

def monthly_challanges(request, month):
   try:
    result = monthly_challanges_list[month]
    return HttpResponse(result)
   except:
      return HttpResponseNotFound("No response for this request")

def pages(request, pageNo):
   return HttpResponse(f'Dang Dang {pageNo} Bro')