from django.shortcuts import render

# ログイン前ホーム画面
def index(request):
    return render(request, '1index.html')

# ログイン画面
def userlogin(request):
    return render(request, '1userlogin.html')

# ログアウト画面
def logout(request):
    return render(request, '1logout.html')

# 新規登録画面
def usersignup(request):
    return render(request, '1usersignup.html')

# 新規登録完了画面
def signupcompleted(request):
    return render(request, '1signupcompleted.html')
