from django.db import models
import uuid
from django.core.validators import MaxLengthValidator

class User_contactus(models.Model):
    contactus_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contactus_name = models.CharField(max_length=15, validators=[MaxLengthValidator(15)], verbose_name="名前")
    contactus_email = models.EmailField(max_length=50, validators=[MaxLengthValidator(50)], verbose_name="メールアドレス")
    contactus_message = models.TextField(max_length=1000, validators=[MaxLengthValidator(1000)], verbose_name="メッセージ内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    def __str__(self):
        return self.contactus_name
