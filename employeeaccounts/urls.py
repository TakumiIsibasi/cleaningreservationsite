from django.urls import path
from . import views
 
app_name = "employeeaccounts"
 
urlpatterns = [
    path("employeehome", views.employeehome, name="employeehome"),
    path("employeescheduleconfirmation", views.employeescheduleconfirmation, name="employeescheduleconfirmation"),
    path("employeereservationconfirmation", views.employeereservationconfirmation, name="employeereservationconfirmation"),
    path("reservationdetailsconfirmation", views.reservationdetailsconfirmation, name="reservationdetailsconfirmation"),
    path("employeescheduleaddition", views.employeescheduleaddition, name="employeescheduleaddition"),
    path("employeeschedulechange", views.employeeschedulechange, name="employeeschedulechange"),
    path("employeescheduledeletion", views.employeescheduledeletion, name="employeescheduledeletion"),
]
 
 
