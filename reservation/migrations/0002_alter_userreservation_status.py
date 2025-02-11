# Generated by Django 4.2.6 on 2025-02-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreservation',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('canceled', 'Canceled'), ('pending_active', 'pending_active')], default='active', max_length=15, verbose_name='ステータス'),
        ),
    ]
