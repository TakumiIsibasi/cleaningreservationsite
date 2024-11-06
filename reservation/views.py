from django.shortcuts import render

# 利用者ログイン後ホーム画面
def mainmenu(request):
    return render(request, '2mainmenu.html')

# 予約画面
def cleaningappointment(request):
    return render(request, '2cleaningappointment.html')

# 予約完了画面
def reservationcompleted(request):
    return render(request, '2reservationcompleted.html')

# 予約変更画面
def reservationchange(request):
    return render(request, '2reservationchange.html')

# 予約変更完了画面
def reservationchangecompleted(request):
    return render(request, '2reservationchangecompleted.html')

# 予約キャンセル完了画面
def reservationcancellationcompleted(request):
    return render(request, '2reservationcancellationcompleted.html')

# 予約一覧画面
def userreservationlistscreen(request):
    return render(request, '2userreservationlistscreen.html')

# 予約詳細画面
def userreservationdetails(request):
    return render(request, '2userreservationdetails.html')




