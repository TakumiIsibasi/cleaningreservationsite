from django import forms
from .models import UserReservation
from datetime import datetime, timedelta

class UserForm(forms.ModelForm):
    class Meta:
        model = UserReservation
        fields = [
            "user_name",
            "user_phone",
            "user_email",
            "user_address",
            "user_cleaning_location",
            "user_cleaning_date",
            "user_comments"
        ]
        widgets = {
            "user_cleaning_date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",  # Bootstrap などのクラスを適用
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 初期化時には特に制限を加えません
        self.fields['user_cleaning_date'].widget.attrs['min'] = self.get_default_min_date()

    def get_default_min_date(self):
        # デフォルトでは現在の日付 + 3日を設定（変更が必要ならここで設定）
        return (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%dT%H:%M")

    def set_min_date(self, reserved_date):
        # 予約日以降を選べるように設定
        self.fields['user_cleaning_date'].widget.attrs['min'] = reserved_date.strftime("%Y-%m-%dT%H:%M")