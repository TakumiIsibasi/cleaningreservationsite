from django.db import models
import uuid

# Create your models here.
class Admin(models.Model):
    admin_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin_name = models.CharField(max_length=30, verbose_name="名前")
    admin_email = models.EmailField(max_length=50, verbose_name="メールアドレス")
    admin_password = models.CharField(max_length=20, verbose_name="パスワード")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")