# forms.py
from django import forms
from django.contrib.auth import get_user_model  # カスタムユーザーモデルをインポート
from accounts.models import User

#従業員変更
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['name', 'email', 'phone', 'is_active']
        labels = {
            'name': '名前',
            'email': 'メールアドレス',
            'phone': '電話番号',
            'is_active': '在職中'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'role', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
