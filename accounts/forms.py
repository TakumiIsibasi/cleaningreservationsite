from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "phone", "email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # パスワードをハッシュ化して保存
        if commit:
            user.save()
        return user

class SignInForm(forms.Form):
    email = forms.EmailField(
        max_length=50,
        label="メールアドレス",
        widget=forms.EmailInput(attrs={"placeholder": "メールアドレスを入力"}),
    )
    password = forms.CharField(
        max_length=128,
        label="パスワード",
        widget=forms.PasswordInput(attrs={"placeholder": "パスワードを入力"}),
    )