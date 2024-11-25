# models.py
from django.db import models
from django.conf import settings  # カスタムユーザーモデルを使用するために必要

class EmployeeSchedule(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # カスタムユーザーモデルを参照
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True}  # スタッフユーザーのみ選択可能にする
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.employee.name} - {self.date} ({self.start_time} - {self.end_time})'
