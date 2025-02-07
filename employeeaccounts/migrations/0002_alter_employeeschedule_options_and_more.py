# Generated by Django 5.1.2 on 2025-02-07 00:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeaccounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeeschedule',
            options={'ordering': ['date', 'start_time'], 'verbose_name': '従業員スケジュール', 'verbose_name_plural': '従業員スケジュール一覧'},
        ),
        migrations.AlterField(
            model_name='employeeschedule',
            name='date',
            field=models.DateField(verbose_name='勤務日'),
        ),
        migrations.AlterField(
            model_name='employeeschedule',
            name='employee',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='従業員'),
        ),
        migrations.AlterField(
            model_name='employeeschedule',
            name='end_time',
            field=models.TimeField(verbose_name='終了時間'),
        ),
        migrations.AlterField(
            model_name='employeeschedule',
            name='start_time',
            field=models.TimeField(verbose_name='開始時間'),
        ),
        migrations.AlterField(
            model_name='employeeschedule',
            name='task',
            field=models.CharField(max_length=255, verbose_name='作業内容'),
        ),
    ]
