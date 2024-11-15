from django.db import models
import uuid
from django.core.validators import MaxLengthValidator
 
class Employes(models.Model):
    employes_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employes_name = models.CharField(max_length=30, validators=[MaxLengthValidator(30)], verbose_name="名前")
    employes_email = models.EmailField(max_length=50, validators=[MaxLengthValidator(50)], verbose_name="メールアドレス")
    employes_password = models.CharField(max_length=20, validators=[MaxLengthValidator(20)], verbose_name="パスワード")
    employes_status = models.CharField(max_length=10, validators=[MaxLengthValidator(10)], verbose_name="アカウントステータス")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")