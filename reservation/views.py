from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserForm
from .models import UserReservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
 
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
class UserReservationView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserForm()
        return render(request, '2cleaningappointment.html', {"form": form})  
   
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            # フォームが有効な場合は、データを保存してリダイレクト
            reservation = form.save(commit=False)
            reservation.user = request.user  # ログイン中のユーザーを設定
            reservation.save()  # 予約を保存
            return redirect("reservation:reservationcompleted")
        else:
            # フォームが無効な場合は、エラー内容をコンソールに表示
            print("フォームのバリデーションエラー")
            print(form.errors)  # エラー内容を表示
        return render(request, '2cleaningappointment.html', {"form": form})
 
 
 
# 予約一覧画面
class UserReservationListView(LoginRequiredMixin, View):
    def get(self, request):
        Reservation_list = UserReservation.objects.filter(user=request.user)  # ログインユーザーに関連付け
        return render(request, '2userreservationlistscreen.html', {"Reservation_list": Reservation_list})
 
    def post(self, request):
        return self.get(request)
 
 
# 予約詳細画面
class UserReservationDetailView(LoginRequiredMixin, View):
    def get(self, request, user_reservation_id):
        reservation = get_object_or_404(UserReservation, user_reservation_id=user_reservation_id)
        return render(request, "2userreservationdetails.html", {"user_reservation": reservation})
 
 
# 予約変更画面
class UserReservationUpdateView(LoginRequiredMixin, View):
    def get(self, request, user_reservation_id):
        reservation = get_object_or_404(UserReservation, user_reservation_id=user_reservation_id)
        form = UserForm(instance=reservation)
        return render(request, "2reservationchange.html", {
            "form": form,
            "user_reservation_id": user_reservation_id
        })
 
    def post(self, request, user_reservation_id):
        reservation = get_object_or_404(UserReservation, user_reservation_id=user_reservation_id)
        form = UserForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect("reservation:Reservation_detail", user_reservation_id=user_reservation_id)
        return render(request, "2reservationchange.html", {"form": form, "user_reservation_id": user_reservation_id})
       
# URL設定で利用するビューエイリアス
cleaningappointment = UserReservationView.as_view()  # 予約画面
Reservation_list = UserReservationListView.as_view()  # 予約一覧画面
Reservation_detail = UserReservationDetailView.as_view()  # 予約詳細画面
Reservation_update = UserReservationUpdateView.as_view()  # 予約変更画面