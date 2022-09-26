from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path("<int:month>",views.monthly_by_num),
    path("<str:month>",views.monthly_challenge),
   
]
