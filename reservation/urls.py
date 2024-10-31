from django.urls import path
from . import views

urlpatterns = [
    # ログイン前ホーム画面
    path("", views.index, name="index"),
    # ログイン画面
    path("userlogin", views.userlogin, name="userlogin"),
    # ログイン後ホーム画面
    path("mainmenu", views.mainmenu, name="mainmenu"),
    # 新規登録画面
    path("usersignup", views.usersignup, name="usersignup"),
    # 予約画面
    path("cleaningappointment", views.cleaningappointment, name="cleaningappointment"),
    # 予約完了画面
    path("reservationcompleted", views.reservationcompleted, name="reservationcompleted"),
    # 予約詳細画面
    path("userreservationdetails", views.userreservationdetails, name="userreservationdetails"),
    # 予約一覧画面
    path("userreservationlistscreen", views.userreservationlistscreen, name="userreservationlistscreen"),
]