from django.urls import path
from . import views

app_name = "adminaccounts" 

urlpatterns = [
    path("adminhome", views.adminhome, name="adminhome"),
    path("adminemployeelist", views.adminemployeelist, name="adminemployeelist"),
    path("adminrequestconfirmation", views.adminrequestconfirmation, name="adminrequestconfirmation"),
    path("adminemployeeschedulelist", views.adminemployeeschedulelist, name="adminemployeeschedulelist"),
    path("administratorrequestschedulechange", views.administratorrequestschedulechange, name="administratorrequestschedulechange"),
    path("administratorrequestscheduleconfirmation", views.administratorrequestscheduleconfirmation, name="administratorrequestscheduleconfirmation"), 
]