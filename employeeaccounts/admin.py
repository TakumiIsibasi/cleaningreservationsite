from django.contrib import admin
from .models import EmployeeSchedule

@admin.register(EmployeeSchedule)
class EmployeeScheduleAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'start_time', 'end_time', 'task')  # 管理画面に表示するフィールド
    list_filter = ('employee', 'date')  # フィルタリングオプション
    search_fields = ('employee__username', 'task')  # 検索対象
    ordering = ('date', 'start_time')  # 並び順
