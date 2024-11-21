from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid
 
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("メールアドレスは必須です")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        if not extra_fields.get('is_staff'):
            raise ValueError('スーパーユーザーはis_staff=Trueでなければなりません')
        if not extra_fields.get('is_superuser'):
            raise ValueError('スーパーユーザーはis_superuser=Trueでなければなりません')
 
        return self.create_user(email, password, **extra_fields)
 
 
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="名前")
    phone = models.CharField(max_length=12, verbose_name="電話番号")
    email = models.EmailField(unique=True, verbose_name="メールアドレス")
    is_active = models.BooleanField(default=True, verbose_name="有効なユーザーかどうか")
    is_staff = models.BooleanField(default=False, verbose_name="スタッフユーザーかどうか")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
 
    # 問題解消のためのrelated_name設定
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        verbose_name="グループ",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        verbose_name="ユーザー権限",
        blank=True,
    )
 
    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']
 
    def __str__(self):
        return self.name
    
    