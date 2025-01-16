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
        # 現在日から3日後を計算
        min_date = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%dT%H:%M")
        # user_cleaning_date フィールドに min 属性を追加
        self.fields['user_cleaning_date'].widget.attrs['min'] = min_date
