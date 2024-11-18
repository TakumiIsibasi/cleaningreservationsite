from django.db import models
import uuid
from django.core.validators import MaxLengthValidator
from django.contrib.auth.hashers import make_password
 
class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, validators=[MaxLengthValidator(100)], verbose_name="名前")
    phone = models.CharField(max_length=12, validators=[MaxLengthValidator(12)], verbose_name="電話番号")
    email = models.EmailField(max_length=50, validators=[MaxLengthValidator(50)], primary_key=True, verbose_name="メールアドレス")
    password = models.CharField(max_length=128, validators=[MaxLengthValidator(128)], verbose_name="パスワード")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
 
    def __str__(self):
        return self.name
 
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()
 
        #ハッシュ化にこれをつかうらしい↑↓
        #user = User(name="example_name", phone="1234567890", email="example@example.com", address="Some Address")
        #user.set_password("plain_text_password")  # ハッシュ化されたパスワードを設定
        #user.save()
