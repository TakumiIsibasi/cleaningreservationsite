from django.urls import path
from . import views

urlpatterns = [
    # ログイン前ホーム画面
    path("", views.index, name="index"),
    # ログイン画面
    path("userlogin", views.userlogin, name="userlogin"),
    # ログイン後ホーム画面
    path("mainmenu", views.mainmenu, name="mainmenu"),
    # ログアウト画面
    path("logout", views.logout, name="logout"),
    # 新規登録画面
    path("usersignup", views.usersignup, name="usersignup"),
    # 新規登録完了画面
    path("signupcompleted", views.signupcompleted, name="signupcompleted"),
    # 予約画面
    path("cleaningappointment", views.cleaningappointment, name="cleaningappointment"),
    # 予約完了画面
    path("reservationcompleted", views.reservationcompleted, name="reservationcompleted"),
    #予約変更画面
    path("reservationchange", views.reservationchange, name="reservationchange"),
    #予約変更完了画面
    path("reservationchangecompleted", views.reservationchangecompleted, name="reservationchangecompleted"),
    #予約キャンセル完了画面
    path("reservationcancellationcompleted", views.reservationcancellationcompleted, name="reservationcancellationcompleted"),
    # 予約一覧画面
    path("userreservationlistscreen", views.userreservationlistscreen, name="userreservationlistscreen"),
    # 予約詳細画面
    path("userreservationdetails", views.userreservationdetails, name="userreservationdetails"),  
]