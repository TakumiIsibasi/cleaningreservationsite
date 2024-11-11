# プロジェクトのurls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # これは元からある
    path("", include("accounts.urls")),  # accountsアプリのurls
    path("reservation/", include("reservation.urls")),  # reservationのurls
    path("contactus/", include("contactus.urls")),  # contactusのurls
]
