from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index), #challenges/
    path("<int:month>",views.monthly_by_num,name="month-int"),#challenges/1
    path("<str:month>",views.monthly_challenge,name="month-challenge"),#challenges/jan
   
]
