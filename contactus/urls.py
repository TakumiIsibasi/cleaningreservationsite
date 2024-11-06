from django.urls import path
from . import views

urlpatterns = [
    # お問い合わせ画面
    path("", views.contactus, name="contactus"),
    # お問い合わせ送信完了画面
    path("submissioncomplete", views.submissioncomplete, name="submissioncomplete"),
]