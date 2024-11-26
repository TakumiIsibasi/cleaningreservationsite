# Generated by Django 4.2.6 on 2024-11-26 01:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReservation',
            fields=[
                ('user_reservation_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50)], verbose_name='名前')),
                ('user_phone', models.CharField(max_length=12, validators=[django.core.validators.MaxLengthValidator(12)], verbose_name='電話番号')),
                ('user_email', models.EmailField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50)], verbose_name='メールアドレス')),
                ('user_address', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50)], verbose_name='住所')),
                ('user_cleaning_location', models.TextField(max_length=100, validators=[django.core.validators.MaxLengthValidator(100)], verbose_name='清掃場所')),
                ('user_cleaning_date', models.DateTimeField(verbose_name='清掃時間')),
                ('user_comments', models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)], verbose_name='備考欄')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('request_date', models.DateField(auto_now_add=True, verbose_name='予約日')),
                ('approval_date', models.DateField(blank=True, null=True, verbose_name='許可日')),
                ('status', models.CharField(choices=[('active', 'Active'), ('canceled', 'Canceled')], default='active', max_length=10, verbose_name='ステータス')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL, verbose_name='予約したユーザー')),
            ],
        ),
    ]
