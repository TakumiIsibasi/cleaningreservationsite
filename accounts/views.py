from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from .models import User

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
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'testusersignup.html', {"form": form})  
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # フォームデータを保存
            return redirect("signupcompleted")  # 新規登録完了ページへリダイレクト
        else:
            print(form.errors)  # バリデーションエラーメッセージを出力    
        return render(request, 'testusersignup.html', {"form": form})  

# 新規登録完了画面
def signupcompleted(request):
    return render(request, '1signupcompleted.html')

usersignup = SignUpView.as_view()