from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserForm
from .models import UserReservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def mainmenu(request):
    return render(request, '2mainmenu.html')

@login_required
def reservationcompleted(request):
    return render(request, '2reservationcompleted.html')

class ReservationCancellationCompletedView(LoginRequiredMixin, View):
    def post(self, request, user_reservation_id):
        reservation = get_object_or_404(UserReservation, pk=user_reservation_id, user=request.user)
        reservation.status = 'canceled'
        reservation.save()
        return redirect('reservation:reservationcancellationcompleted', user_reservation_id=user_reservation_id)
    
    def get(self, request, user_reservation_id):
        # GETリクエストの場合、予約一覧にリダイレクト
        return redirect('reservation:Reservation_list')

class UserReservationListView(LoginRequiredMixin, View):
    def get(self, request):
        Reservation_list = UserReservation.objects.filter(user=request.user, status='active')
        return render(request, '2userreservationlistscreen.html', {"Reservation_list": Reservation_list})
    
    def post(self, request):
        return self.get(request)

class UserReservationDetailView(LoginRequiredMixin, View):
    def get(self, request, user_reservation_id):
        reservation = get_object_or_404(UserReservation, user_reservation_id=user_reservation_id, user=request.user)
        return render(request, "2userreservationdetails.html", {"user_reservation": reservation})

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

cleaningappointment = ReservationCancellationCompletedView.as_view()
Reservation_list = UserReservationListView.as_view()
Reservation_detail = UserReservationDetailView.as_view()
Reservation_update = UserReservationUpdateView.as_view()
