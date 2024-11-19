from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
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
 
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, '1userlogin.html', {
                'form': form,
                'error_message': "メールアドレスまたはパスワードが正しくありません。",
            })
 
        # パスワード検証
        if check_password(password, user.password):
            # ログイン成功後、reservation:mainmenuにリダイレクト
            return redirect('reservation:mainmenu')  
        else:
            return render(request, '1userlogin.html', {
                'form': form,
                'error_message': "メールアドレスまたはパスワードが正しくありません。",
            })
 
    return render(request, '1userlogin.html', {'form': form})
 
# ログアウト画面
def logout(request):
    return render(request, '1logout.html')
 
# 新規登録画面
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, '1usersignup.html', {"form": form})  
   
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # フォームデータを保存
            return redirect("signupcompleted")  # 新規登録完了ページへリダイレクト
        else:
            print(form.errors)  # バリデーションエラーメッセージを出力    
        return render(request, '1usersignup.html', {"form": form})  
 
# 新規登録完了画面
def signupcompleted(request):
    return render(request, '1signupcompleted.html')
 
usersignup = SignUpView.as_view()