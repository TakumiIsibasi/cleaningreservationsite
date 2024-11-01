from django.shortcuts import render

# ログイン前ホーム画面
def index(request):
    return render(request, 'index.html')

# ログイン画面
def userlogin(request):
    return render(request, 'userlogin.html')

# ログイン後ホーム画面
def mainmenu(request):
    return render(request, 'mainmenu.html')

# ログアウト画面
def logout(request):
    return render(request, 'logout.html')

# 新規登録画面
def usersignup(request):
    return render(request, 'usersignup.html')

# 新規登録完了画面
def signupcompleted(request):
    return render(request, 'signupcompleted.html')

# 予約画面
def cleaningappointment(request):
    return render(request, 'cleaningappointment.html')

# 予約完了画面
def reservationcompleted(request):
    return render(request, 'reservationcompleted.html')

# 予約変更画面
def reservationchange(request):
    return render(request, 'reservationchange.html')

# 予約変更完了画面
def reservationchangecompleted(request):
    return render(request, 'reservationchangecompleted.html')

# 予約キャンセル完了画面
def reservationcancellationcompleted(request):
    return render(request, 'reservationcancellationcompleted.html')

# 予約一覧画面
def userreservationlistscreen(request):
    return render(request, 'userreservationlistscreen.html')

# 予約詳細画面
def userreservationdetails(request):
    return render(request, 'userreservationdetails.html')

# お問い合わせ画面
def contactus(request):
    return render(request, 'contactus.html')

# お問い合わせ送信完了画面
def submissioncomplete(request):
    return render(request, 'submissioncomplete.html')


