from django.urls import path
from . import views

app_name = "contactus"

urlpatterns = [
    path("", views.ContactUsCreateView.as_view(), name="contactus_create"),
    path("submissioncomplete/", views.submissioncomplete, name="submissioncomplete"),
]
