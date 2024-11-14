from django.urls import path
from . import views

app_name = "employeeaccounts" 

urlpatterns = [
    path("employeereservationconfirmation", views.employeereservationconfirmation, name="employeereservationconfirmation"),
    path("employeescheduleaddition", views.employeescheduleaddition, name="employeescheduleaddition"),
    path("employeeschedulechange", views.employeeschedulechange, name="employeeschedulechange"),
    path("employeescheduleconfirmation", views.employeescheduleconfirmation, name="employeescheduleconfirmation"),
    path("administratorrequestschedulechange", views.administratorrequestschedulechange, name="administratorrequestschedulechange"),
    path("administratorrequestscheduleconfirmation", views.administratorrequestscheduleconfirmation, name="administratorrequestscheduleconfirmation"), 
]
