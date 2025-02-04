# forms.py
from django import forms
from django.contrib.auth import get_user_model  # カスタムユーザーモデルをインポート

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
