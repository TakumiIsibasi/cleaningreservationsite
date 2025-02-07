from django.urls import path
from . import views

app_name = "adminaccounts" 

urlpatterns = [
    path("", views.adminhome, name="adminhome"),
    path("adminemployeelist", views.adminemployeelist, name="adminemployeelist"),
    path("adminrequestconfirmation", views.adminrequestconfirmation, name="adminrequestconfirmation"),
    path("adminemployeeschedulelist", views.adminemployeeschedulelist, name="adminemployeeschedulelist"),
    path("administratorrequestschedulechange", views.administratorrequestschedulechange, name="administratorrequestschedulechange"),
    path("administratorrequestscheduleconfirmation", views.administratorrequestscheduleconfirmation, name="administratorrequestscheduleconfirmation"), 
    path("employee_update/<uuid:employee_id>/", views.employee_update, name="employee_update"), 
    path("adminrequestconfirmation/", views.adminrequestconfirmation, name='adminrequestconfirmation'),
    path("adminemployeeschedulelist/", views.adminemployeeschedulelist, name='adminemployeeschedulelist'),
    path('employee/add/', views.add_employee, name='employee_add'),
]