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
def index(request):
    list_items=""
    months=list(monthly_challenges.keys())
    for month in months:
        cap_month=month.capitalize()
        month_path=reverse("month-challenge",args=[month])
        list_items+= f"<li><a href=\"{month_path}\">{cap_month}</a></li>"
    response_data=f"""
    <h1>
    <ul>
        {list_items}
    </ul>
    </h1>
    """
    return HttpResponse(response_data)





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
        response_data=f"<h1>{text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Not found</h1>")
   

    