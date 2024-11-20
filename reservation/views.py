from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserForm
from .models import user_reservation
from django.contrib.auth.decorators import login_required

# 利用者ログイン後のホーム画面
# ユーザーがログイン後にアクセスするメインメニューを表示するビュー
@login_required
def mainmenu(request):
    return render(request, '2mainmenu.html')

# 予約完了画面
# 予約が正常に完了した際に表示されるページ
def reservationcompleted(request):
    return render(request, '2reservationcompleted.html')

# 予約変更画面
# 予約を変更するためのフォームを表示するページ
def reservationchange(request):
    return render(request, '2reservationchange.html')

# 予約変更完了画面
# 予約の変更が完了したことを知らせるページ
def reservationchangecompleted(request):
    return render(request, '2reservationchangecompleted.html')

# 予約キャンセル完了画面
# 予約のキャンセルが正常に完了したことを知らせるページ
def reservationcancellationcompleted(request):
    return render(request, '2reservationcancellationcompleted.html')

# 予約詳細画面
# ユーザーが自身の予約内容を確認するためのページ
def userreservationdetails(request):
    return render(request, '2userreservationdetails.html')


# 予約画面
# ユーザーが新しいクリーニング予約を行うためのフォームを提供するクラスベースのビュー
class UserReservationView(View):
    # GETリクエスト時に予約フォームを表示
    def get(self, request):
        form = UserForm()
        return render(request, '2cleaningappointment.html', {"form": form})  
    
    # POSTリクエスト時にフォームのデータを処理
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():  # バリデーションチェック
            form.save()  # フォームデータを保存
            return redirect("reservation:reservationcompleted")  # 予約完了ページへリダイレクト
        else:
            print(form.errors)  # バリデーションエラーをコンソールに出力    
        return render(request, '2cleaningappointment.html', {"form": form})  


# 予約一覧画面
# ユーザーがこれまでの予約のリストを確認するためのクラスベースのビュー
class UserReservationListView(View):
    # GETリクエスト時に全ての予約を取得して表示
    def get(self, request):
        Reservation_list = user_reservation.objects.all()
        return render(request, '2userreservationlistscreen.html', {"Reservation_list": Reservation_list})

    # POSTリクエストを処理（必要に応じて）
    # 例: 予約のフィルタリングや削除操作など
    def post(self, request):
        return self.get(request)  # POST処理後に一覧を再描画

# 予約詳細画面
# 特定の予約の詳細を表示するためのクラスベースのビュー
class UserReservationDetailView(View):
    def get(self, request, user_reservation_id):
        # 指定されたIDの予約を取得（存在しない場合は404エラー）
        reservation = get_object_or_404(user_reservation, user_reservation_id=user_reservation_id)
        return render(request, "2userreservationdetails.html", {"user_reservation": reservation})

# 予約変更画面
# 既存の予約を編集するためのクラスベースのビュー
class UserReservationUpdateView(View):
    # GETリクエスト時に編集用フォームを表示
    def get(self, request, user_reservation_id):
        reservation = get_object_or_404(user_reservation, user_reservation_id=user_reservation_id)
        form = UserForm(instance=reservation)  # 既存データをフォームに設定
        return render(request, "2reservationchange.html", {
            "form": form, 
            "user_reservation_id": user_reservation_id
        })

    # POSTリクエスト時にフォームのデータを処理
    def post(self, request, user_reservation_id):
        reservation = get_object_or_404(user_reservation, user_reservation_id=user_reservation_id)
        form = UserForm(request.POST, instance=reservation)  # フォームを更新モードで作成
        if form.is_valid():  # バリデーションチェック
            form.save()  # データを保存
            return redirect("reservation:Reservation_detail", user_reservation_id=user_reservation_id)
        return render(request, "2reservationchange.html", {"form": form, "user_reservation_id": user_reservation_id})


# URL設定で利用するビューエイリアス
cleaningappointment = UserReservationView.as_view()  # 予約画面
Reservation_list = UserReservationListView.as_view()  # 予約一覧画面
Reservation_detail = UserReservationDetailView.as_view()  # 予約詳細画面
Reservation_update = UserReservationUpdateView.as_view()  # 予約変更画面
