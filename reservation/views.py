from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserForm
from .models import UserReservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
 
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserForm
from .models import UserReservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# 利用者ログイン後のホーム画面
@login_required
def mainmenu(request):
    return render(request, '2mainmenu.html')

# 予約キャンセル完了画面
@login_required
def reservationcancellationcompleted(request, user_reservation_id):
    # 指定された予約を取得し、ステータスをキャンセルに変更
    reservation = get_object_or_404(UserReservation, pk=user_reservation_id, user=request.user)
    reservation.status = "canceled"
    reservation.save()
    return render(request, '2reservationcancellationcompleted.html')

# 予約完了画面
@login_required
def reservationcompleted(request):
    return render(request, '2reservationcompleted.html')

# 予約詳細画面
@login_required
def userreservationdetails(request):
    return render(request, '2userreservationdetails.html')

# 予約画面
class UserReservationView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserForm()
        return render(request, '2cleaningappointment.html', {"form": form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect("reservation:reservationcompleted")
        else:
            print("フォームのバリデーションエラー")
            print(form.errors)
        return render(request, '2cleaningappointment.html', {"form": form})

# 予約一覧画面
class UserReservationListView(LoginRequiredMixin, View):
    def get(self, request):
        Reservation_list = UserReservation.objects.filter(user=request.user)
        return render(request, '2userreservationlistscreen.html', {"Reservation_list": Reservation_list})

    def post(self, request):
        return self.get(request)

# 予約詳細画面
class UserReservationDetailView(LoginRequiredMixin, View):
    def get(self, request, user_reservation_id):
        reservation = get_object_or_404(UserReservation, user_reservation_id=user_reservation_id, user=request.user)
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