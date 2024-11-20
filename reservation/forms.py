from django import forms
from .models import user_reservation

# 予約用フォーム
# モデル`user_reservation`に基づくフォームを作成
class UserForm(forms.ModelForm):
    class Meta:
        # 使用するモデルを指定
        model = user_reservation
        
        # フォームに含めるフィールドを指定
        fields = [
            "user_name",             # ユーザーの名前
            "user_phone",            # ユーザーの電話番号
            "user_email",            # ユーザーのメールアドレス
            "user_addres",           # ユーザーの住所
            "user_cleaning_location",# 清掃の実施場所
            "user_cleaning_date",    # 清掃の希望日時
            "user_comments"          # 備考欄
        ]
