from django.urls import path
from . import views

app_name = "reservation" 

urlpatterns = [
    path("mainmenu", views.mainmenu, name="mainmenu"), 
    path("cleaningappointment", views.cleaningappointment, name="cleaningappointment"),
    path("reservationcompleted", views.reservationcompleted, name="reservationcompleted"),
    path("reservationchange", views.reservationchange, name="reservationchange"),
    path("reservationchangecompleted", views.reservationchangecompleted, name="reservationchangecompleted"),
    path("reservationcancellationcompleted", views.reservationcancellationcompleted, name="reservationcancellationcompleted"),
    path("Reservation_list", views.Reservation_list, name="Reservation_list"),
    path("userreservationdetails", views.userreservationdetails, name="userreservationdetails"),  
]
