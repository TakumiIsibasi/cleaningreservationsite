from django.urls import path
from . import views

# アプリ名の設定
app_name = "reservation" 

# URLパターンの定義
urlpatterns = [
     path("mainmenu", views.mainmenu, name="mainmenu"),
    path("cleaningappointment", views.cleaningappointment, name="cleaningappointment"),
    path("reservationcompleted", views.reservationcompleted, name="reservationcompleted"),
    # reservationchangecompletedは不要なので削除
    # path("reservationchangecompleted", views.reservationchangecompleted, name="reservationchangecompleted"), 
    path("reservationcancellationcompleted/<uuid:user_reservation_id>", views.reservationcancellationcompleted, name="reservationcancellationcompleted"),
    path("Reservation_list", views.Reservation_list, name="Reservation_list"),
    path("Reservation_detail/<uuid:user_reservation_id>", views.Reservation_detail, name="Reservation_detail"),
    path("Reservation_update/<uuid:user_reservation_id>/update", views.Reservation_update, name="Reservation_update"),
]
