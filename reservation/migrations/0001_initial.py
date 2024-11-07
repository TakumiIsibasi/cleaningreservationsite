# Generated by Django 4.2.6 on 2024-11-07 01:56

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_reservation',
            fields=[
                ('user_reservation_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50)], verbose_name='名前')),
                ('user_phone', models.IntegerField(max_length=12, validators=[django.core.validators.MaxLengthValidator(12)], verbose_name='電話番号')),
                ('user_email', models.EmailField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50)], verbose_name='メールアドレス')),
                ('user_addres', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50)], verbose_name='住所')),
                ('user_cleaning_location', models.TextField(max_length=100, validators=[django.core.validators.MaxLengthValidator(100)], verbose_name='清掃場所')),
                ('user_cleaning_date', models.DateTimeField(verbose_name='清掃時間')),
                ('user_comments', models.TextField(max_length=300, validators=[django.core.validators.MaxLengthValidator(300)], verbose_name='備考欄')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('request_date', models.DateField(auto_now_add=True, verbose_name='予約日')),
                ('approval_date', models.DateField(auto_now=True, verbose_name='許可日')),
            ],
        ),
    ]
