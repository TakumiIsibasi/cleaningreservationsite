from django.db import models
import uuid

class UserReservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_email = models.EmailField()
    user_address = models.TextField()
    user_cleaning_location = models.CharField(max_length=255)
    user_cleaning_date = models.DateTimeField()
    
    STATUS_CHOICES = [
        ('active', '有効'),
        ('cancelled', 'キャンセル'),
        ('approved', '許可'),  # 許可ステータスを追加
    ]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.user_name} - {self.user_cleaning_date.strftime('%Y-%m-%d %H:%M')} - {self.get_status_display()}"
