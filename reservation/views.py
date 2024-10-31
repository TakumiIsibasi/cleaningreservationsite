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

# 新規登録画面
def usersignup(request):
    return render(request, 'usersignup.html')

# 予約画面
def cleaningappointment(request):
    return render(request, 'cleaningappointment.html')

# 予約完了画面
def reservationcompleted(request):
    return render(request, 'reservationcompleted.html')

# 予約詳細画面
def userreservationdetails(request):
    return render(request, 'userreservationdetails.html')

# 予約一覧画面
def userreservationlistscreen(request):
    return render(request, 'userreservationlistscreen.html')