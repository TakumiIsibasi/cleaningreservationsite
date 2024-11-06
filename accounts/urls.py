from django.urls import path
from . import views

urlpatterns = [
    # ログイン前ホーム画面
    path("", views.index, name="index"),
    # ログイン画面
    path("userlogin", views.userlogin, name="userlogin"),
    # ログアウト画面
    path("logout", views.logout, name="logout"),
    # 新規登録画面
    path("usersignup", views.usersignup, name="usersignup"),
    # 新規登録完了画面
    path("signupcompleted", views.signupcompleted, name="signupcompleted"),
]