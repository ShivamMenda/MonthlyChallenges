from django.http import Http404, HttpResponseNotFound,HttpResponseRedirect
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
    "dec":None,
}

# Create your views here.
def index(request):
    months=list(monthly_challenges.keys())
    return render(request,"challenges/index.html",{
        "months": months
    })

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
        return render(request,"challenges/challenge.html",{
            "text":text,
            "month_name":month,
            })
    except:
        raise Http404() #Best way to render 404 looks for 404 in the templates folder in root.
   

    