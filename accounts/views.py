from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout as auth_logout, authenticate
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, SignInForm
from .models import User


# ログイン前ホーム画面
def index(request):
    return render(request, '1index.html')


# ログイン画面
def userlogin(request):
    form = SignInForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        # ユーザー認証
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)  # ログイン処理
            return redirect('reservation:mainmenu')  # ログイン成功後メインメニューへリダイレクト
        else:
            return render(request, '1userlogin.html', {
                'form': form,
                'error_message': "メールアドレスまたはパスワードが正しくありません。",
            })

    return render(request, '1userlogin.html', {'form': form})


# ログアウト画面
def logout(request):
    auth_logout(request)  # ログアウト処理
    return render(request, '1logout.html')


# 新規登録画面
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, '1usersignup.html', {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # フォームデータを保存
            login(request, user)  # 新規登録後自動ログイン
            return redirect("signupcompleted")  # 新規登録完了ページへリダイレクト
        else:
            print(form.errors)  # バリデーションエラーメッセージを出力
        return render(request, '1usersignup.html', {"form": form})


# 新規登録完了画面
def signupcompleted(request):
    return render(request, '1signupcompleted.html')


usersignup = SignUpView.as_view()
