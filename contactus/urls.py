# urls.py
from django.urls import path
from . import views

app_name = "contactus"

urlpatterns = [
    # お問い合わせ画面
    path("", views.ContactusCreateView.as_view(), name="contactus_create"),
    # お問い合わせ送信完了画面
    path("submissioncomplete/", views.submissioncomplete, name="submissioncomplete"),
]
