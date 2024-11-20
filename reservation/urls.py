from django.urls import path
from . import views

# アプリ名の設定
app_name = "reservation" 

# URLパターンの定義
urlpatterns = [
    # メインメニュー画面
    # ユーザーがログイン後にアクセスするメインページ
    path("mainmenu", views.mainmenu, name="mainmenu"), 
    
    # 予約画面
    # 新規のクリーニング予約を作成するためのフォームを表示
    path("cleaningappointment", views.cleaningappointment, name="cleaningappointment"),
    
    # 予約完了画面
    # 新規予約が正常に完了したことを知らせるページ
    path("reservationcompleted", views.reservationcompleted, name="reservationcompleted"),
    
    # 予約変更完了画面
    # 既存予約の変更が正常に完了したことを知らせるページ
    path("reservationchangecompleted", views.reservationchangecompleted, name="reservationchangecompleted"),
    
    # 予約キャンセル完了画面
    # 予約のキャンセルが完了したことを知らせるページ
    path("reservationcancellationcompleted", views.reservationcancellationcompleted, name="reservationcancellationcompleted"),
    
    # 予約一覧画面
    # ユーザーが過去の予約や現在の予約を一覧表示するページ
    path("Reservation_list", views.Reservation_list, name="Reservation_list"),
    
    # 予約詳細画面
    # 特定の予約の詳細情報を表示するページ
    # <uuid:user_reservation_id> は予約を識別するためのID
    path("Reservation_detail/<uuid:user_reservation_id>", views.Reservation_detail, name="Reservation_detail"),
    
    # 予約変更画面
    # 特定の予約を編集するためのフォームを提供するページ
    # <uuid:user_reservation_id> は変更対象の予約を識別
    path("Reservation_update/<uuid:user_reservation_id>/update", views.Reservation_update, name="Reservation_update"),
]
