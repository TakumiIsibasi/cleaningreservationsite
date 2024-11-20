from django.db import models
import uuid
from django.core.validators import MaxLengthValidator

class user_reservation(models.Model):
    # 主キーとしてUUIDを使用（自動生成される）
    user_reservation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # ユーザーの名前（最大50文字、バリデータで50文字に制限）
    user_name = models.CharField(max_length=50, validators=[MaxLengthValidator(50)], verbose_name="名前")
    
    # ユーザーの電話番号（最大12文字、バリデータで12文字に制限）
    user_phone = models.CharField(max_length=12, validators=[MaxLengthValidator(12)], verbose_name="電話番号")
    
    # ユーザーのメールアドレス（最大50文字、バリデータで50文字に制限）
    user_email = models.EmailField(max_length=50, validators=[MaxLengthValidator(50)], verbose_name="メールアドレス")
    
    # ユーザーの住所（最大50文字、バリデータで50文字に制限）
    user_addres = models.CharField(max_length=50, validators=[MaxLengthValidator(50)], verbose_name="住所")
    
    # 清掃場所の情報（最大100文字、バリデータで100文字に制限）
    user_cleaning_location = models.TextField(max_length=100, validators=[MaxLengthValidator(100)], verbose_name="清掃場所")
    
    # 清掃日時（日時を指定、バリデータなし）
    user_cleaning_date = models.DateTimeField(verbose_name="清掃時間")
    
    # 備考欄（最大300文字、バリデータで300文字に制限）
    user_comments = models.TextField(max_length=300, validators=[MaxLengthValidator(300)], verbose_name="備考欄")
    
    # 予約が作成された日時（自動で設定）
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    
    # 予約が最後に更新された日時（自動で更新）
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    # 予約を行った日（日付のみ）
    request_date = models.DateField(auto_now_add=True, verbose_name="予約日")
    
    # 予約が許可された日（日付のみ）
    approval_date = models.DateField(auto_now=True, verbose_name="許可日")

    # 予約のユーザー名を表示する（管理画面などで使用）
    def __str__(self):
        return self.user_name
