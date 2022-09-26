from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
monthly_challenges={
    "jan":"Challenge 1",
    "feb":"Challenge 2",
    "mar":"Challenge 3",
    "apr":"Challenge 4",
    "may":"Challenge 5",
    "june":"Challenge 6",
    "july":"Challenge 7",
    "august":"Challenge 8",
    "sep":"Challenge 9",
    "oct":"Challenge 10",
    "nov":"Challenge 11",
    "dec":"Challenge 12",
}

# Create your views here.
def monthly_by_num(request,month):
    months=list(monthly_challenges.keys())
    if(month>len(months)):
        return HttpResponseNotFound("Invalid")
    redirect_month=months[month-1]
    redirect_path=reverse("month-challenge",args=[redirect_month]) #/challenges/month Reverse function
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        text=monthly_challenges[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Not found")
   

    