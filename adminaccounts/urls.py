from django.urls import path
from . import views

app_name = "adminaccounts" 

urlpatterns = [
    path("", views.adminhome, name="adminhome"),
    path("adminemployeelist/", views.adminemployeelist, name="adminemployeelist"),
    path("adminrequestconfirmation/", views.adminrequestconfirmation, name="adminrequestconfirmation"),
    path("adminemployeeschedulelist/", views.adminemployeeschedulelist, name="adminemployeeschedulelist"),
    path("administratorrequestschedulechange/", views.administratorrequestschedulechange, name="administratorrequestschedulechange"),
    path("administratorrequestscheduleconfirmation/", views.administratorrequestscheduleconfirmation, name="administratorrequestscheduleconfirmation"), 
    path("employee/update/<uuid:employee_id>/", views.employee_update, name="employee_update"), 
    path("employee/add/", views.add_employee, name="employee_add"),
    path("employee/delete/<uuid:employee_id>/", views.delete_employee, name="employee_delete"), 
    path("reservation/update/<uuid:reservation_id>/", views.update_reservation_status, name="update_reservation_status"),

]
