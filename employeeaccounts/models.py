from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
 
 
class EmployeeSchedule(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': True},
        verbose_name="従業員"
    )
    date = models.DateField(verbose_name="勤務日")
    start_time = models.TimeField(verbose_name="開始時間")
    end_time = models.TimeField(verbose_name="終了時間")
    task = models.CharField(max_length=255, verbose_name="作業内容")
 
    class Meta:
        verbose_name = "従業員スケジュール"
        verbose_name_plural = "従業員スケジュール一覧"
        ordering = ['date', 'start_time']
 
    def clean(self):
        # 開始時間が終了時間より後にならないように検証
        if self.start_time >= self.end_time:
            raise ValidationError("開始時間は終了時間より前でなければなりません。")
 
    def __str__(self):
        return f'{self.employee.get_full_name() or self.employee.username} - {self.date} ({self.start_time} - {self.end_time})'