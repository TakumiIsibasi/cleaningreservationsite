from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm
from .models import User


# ログイン前ホーム画面
def index(request):
    return render(request, '1index.html')


# ログイン画面
def userlogin(request):
    form = SignInForm(request.POST or None)
    error_message = None

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        # ユーザー認証
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)  # ログイン処理

            # ログイン後のリダイレクト処理
            if user.is_admin:  # 管理者用ページ
                return redirect('adminaccounts:adminhome')
            elif user.is_staff_member:  # 従業員用ページ
                return redirect('staff_dashboard')
            else:  # 顧客用ページ
                return redirect('reservation:mainmenu')
        else:
            error_message = "メールアドレスまたはパスワードが正しくありません。"

    return render(request, '1userlogin.html', {
        'form': form,
        'error_message': error_message,
    })



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
            return redirect('login_redirect')  # ログインリダイレクトビューへ
        else:
            print(form.errors)  # バリデーションエラーメッセージを出力
        return render(request, '1usersignup.html', {"form": form})


# 新規登録完了画面
def signupcompleted(request):
    return render(request, '1signupcompleted.html')


# リダイレクト用ビュー
@login_required
def login_redirect_view(request):
    user = request.user

    if hasattr(user, 'is_admin') and user.is_admin:
        return redirect('1signupcompleted.html')  # 管理者用ページ
    elif hasattr(user, 'is_staff_member') and user.is_staff_member:
        return redirect('staff_dashboard')  # 従業員用ページ
    else:
        return redirect('customer_dashboard')  # 顧客用ページ


# クラスビューのインスタンス化
usersignup = SignUpView.as_view()
