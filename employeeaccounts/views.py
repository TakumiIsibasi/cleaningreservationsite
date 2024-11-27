from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmployeeScheduleForm
from .models import EmployeeSchedule

# 従業員ホーム
def employeehome(request):
    return render(request, '4employeehome.html')
 
# 従業員スケジュールメニュー
def employeescheduleconfirmation(request):
    # 全ての従業員のスケジュールを取得
    schedules = EmployeeSchedule.objects.all().order_by('date', 'start_time')
    return render(request, '4employeescheduleconfirmation.html', {'schedules': schedules})
 
# 清掃依頼確認
def employeereservationconfirmation(request):
    return render(request, '4employeereservationconfirmation.html')
 
# 清掃依頼詳細確認
def reservationdetailsconfirmation(request):
    return render(request, '4reservationdetailsconfirmation.html')
 
# スケジュール追加
def employeescheduleaddition(request):
    if request.method == 'POST':
        form = EmployeeScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.employee = request.user  # 現在のユーザーを従業員として設定
            schedule.save()
            return redirect('employeeaccounts:employeescheduleconfirmation')  # 確認ページへリダイレクト
    else:
        form = EmployeeScheduleForm()

    return render(request, '4employeescheduleaddition.html', {'form': form})
 
# スケジュール変更
def employeeschedulechange(request):
    schedules = EmployeeSchedule.objects.all().order_by('date', 'start_time')

    if request.method == 'POST':
        schedule_id = request.POST.get('schedule_id')
        schedule = get_object_or_404(EmployeeSchedule, id=schedule_id)

        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        task = request.POST.get('task')

        if date:
            schedule.date = date
        if start_time:
            schedule.start_time = start_time
        if end_time:
            schedule.end_time = end_time
        if task:
            schedule.task = task

        schedule.save()
        messages.success(request, "スケジュールが正常に更新されました。")
        return redirect('employeeaccounts:employeescheduleconfirmation')

    return render(request, '4employeeschedulechange.html', {'schedules': schedules})
 
# スケジュール削除
def employeescheduledeletion(request):
    # スケジュール一覧を取得
    schedules = EmployeeSchedule.objects.all().order_by('date', 'start_time')

    if request.method == 'POST':
        # フォームから削除対象のスケジュールIDを取得
        schedule_id = request.POST.get('schedule_id')
        schedule = get_object_or_404(EmployeeSchedule, id=schedule_id)

        # 削除処理
        schedule.delete()
        messages.success(request, "スケジュールが正常に削除されました。")
        return redirect('employeeaccounts:employeescheduledeletion')

    return render(request, '4employeescheduledeletion.html', {'schedules': schedules})