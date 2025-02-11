from django.db import models
import uuid
from django.conf import settings
from django.core.validators import MaxLengthValidator

class UserReservation(models.Model):
    STATUS_CHOICES = [
        ('active', '許可'),
        ('canceled', 'キャンセル'),
        ('pending_active', '許可待ち'),  # 許可待ち状態を追加
    ]
 
    # 主キーとしてUUIDを使用
    user_reservation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 
    # ユーザーとの関連付け
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name="予約したユーザー"
    )
 
    # ユーザー情報
    user_name = models.CharField(max_length=50, validators=[MaxLengthValidator(50)], verbose_name="名前")
    user_phone = models.CharField(max_length=12, validators=[MaxLengthValidator(12)], verbose_name="電話番号")
    user_email = models.EmailField(max_length=50, validators=[MaxLengthValidator(50)], verbose_name="メールアドレス")
    user_address = models.CharField(max_length=50, validators=[MaxLengthValidator(50)], verbose_name="住所")
 
    # 清掃情報
    user_cleaning_location = models.TextField(max_length=100, validators=[MaxLengthValidator(100)], verbose_name="清掃場所")
    user_cleaning_date = models.DateTimeField(verbose_name="清掃時間")
 
    # 備考欄
    user_comments = models.TextField(max_length=300, validators=[MaxLengthValidator(300)], verbose_name="備考欄", blank=True, null=True)
 
    # 日付情報
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    request_date = models.DateField(auto_now_add=True, verbose_name="予約日")
    approval_date = models.DateField(null=True, blank=True, verbose_name="許可日")
 
    # ステータス
    status = models.CharField(
        max_length=15,  # ステータスの最大文字数を少し大きくしておく
        choices=STATUS_CHOICES,
        default='pending_active',
        verbose_name="ステータス"
    )
 
    def __str__(self):
        return f"{self.user_name} - {self.user_cleaning_date}"

