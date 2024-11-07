from django.urls import path
from . import views

app_name = "reservation" 

urlpatterns = [
    path("reservation:mainmenu", views.mainmenu, name="mainmenu"), 
    path("reservation:cleaningappointment", views.cleaningappointment, name="cleaningappointment"),
    path("reservation:reservationcompleted", views.reservationcompleted, name="reservationcompleted"),
    path("reservation:reservationchange", views.reservationchange, name="reservationchange"),
    path("reservation:reservationchangecompleted", views.reservationchangecompleted, name="reservationchangecompleted"),
    path("reservation:reservationcancellationcompleted", views.reservationcancellationcompleted, name="reservationcancellationcompleted"),
    path("reservation:userreservationlistscreen", views.userreservationlistscreen, name="userreservationlistscreen"),
    path("reservation:userreservationdetails", views.userreservationdetails, name="userreservationdetails"),  
]
