from django.db import models
import uuid

# Create your models here.
class user_reservation(models.Model):
    user_reservation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=50, verbose_name="名前")
    user_phone = models.IntegerField(max_length=12, verbose_name="電話番号")
    user_email = models.EmailField(max_length=50, verbose_name="メールアドレス")
    user_address = models.CharField(max_length=50, verbose_name="住所")
    user_cleaning_location = models.TextField(max_length=100, verbose_name="清掃場所")
    user_cleaning_date = models.DateTimeField(verbose_name="清掃時間")#detetime-localでやってね
    user_comments = models.TextField(max_length=300, verbose_name="備考欄")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    request_date = models.DateField(auto_now_add=True, verbose_name="予約日")
    approval_date = models.DateField(auto_now=True, verbose_name="許可日")

    def __str__(self):
        return self.user_name



