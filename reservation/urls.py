from django.urls import path
from . import views
 
# アプリ名の設定
app_name = "reservation"
 
# URLパターンの定義
urlpatterns = [
    path("mainmenu", views.mainmenu, name="mainmenu"),
    path("cleaningappointment", views.cleaningappointment, name="cleaningappointment"),
    path("reservationcompleted", views.reservationcompleted, name="reservationcompleted"),
    path("reservationcancellationcompleted/<uuid:user_reservation_id>", views.ReservationCancellationCompletedView.as_view(), name="reservationcancellationcompleted"),
    path("Reservation_list", views.UserReservationListView.as_view(), name="Reservation_list"),
    path("Reservation_detail/<uuid:user_reservation_id>", views.Reservation_detail, name="Reservation_detail"),
    path("Reservation_update/<uuid:user_reservation_id>/update", views.Reservation_update, name="Reservation_update"),
]