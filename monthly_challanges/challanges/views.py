from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here

def yearly_challenge(response, year):
    challange_text = None
    if year == "january1":
        challange_text = "Do exexcise for 30 mins at 5 am"
    elif year == "feburary":
        challange_text = "Eat healty Food"
    elif year == "march":
        challange_text = "Learn Django for 20 mins"
    else:
        return HttpResponseNotFound("This response is from yearly challange function")
    return HttpResponse(challange_text)

def monthly_challenges(response, month):
    challange_text = None
    if month == "january":
        challange_text = "Do exexcise for 30 mins"
    elif month == "feburary":
        challange_text = "Eat healty Food"
    elif month == "march":
        challange_text = "Learn Django for 20 mins"
    else:
        return HttpResponseNotFound("No response found for the given request")
    return HttpResponse(challange_text)
