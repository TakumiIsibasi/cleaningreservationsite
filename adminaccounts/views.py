from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import User
from employeeaccounts.models import EmployeeSchedule
from .forms import EmployeeUpdateForm, EmployeeForm 
from reservation.models import UserReservation

# 管理者ホーム画面
def adminhome(request):
    return render(request, '3adminhome.html')

#管理者従業員追加画面
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminaccounts:adminemployeelist')  # リダイレクト修正
    else:
        form = EmployeeForm()
    return render(request, '3add_admin_employee.html', {'form': form})

#管理者作業員削除画面
def delete_employee(request, employee_id):
    employee = get_object_or_404(User, id=employee_id) 
    if request.method == 'POST':
        employee.delete()
        return redirect('adminaccounts:adminemployeelist')  
    return render(request, '3delete_admin_employee.html', {'employee': employee})

# 管理者従業員変更画面
def adminemployeelist(request):
        # スタッフユーザー（従業員）のみを取得
    employees = User.objects.filter(role='staff').order_by('name')

    context = {
        'employees': employees,
    }
    return render(request, '3adminemployeelist.html', context)

def employee_update(request, employee_id):
    employee = get_object_or_404(User, id=employee_id)
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('adminaccounts:adminemployeelist')  # 修正済み
    else:
        form = EmployeeUpdateForm(instance=employee)
    return render(request, '3employee_update.html', {'form': form, 'employee': employee})

# 依頼管理画面
def adminrequestconfirmation(request):
    reservations = UserReservation.objects.filter(status='pending_active').order_by('-created_at')  # 'pending_active'ステータスのものだけ表示
    context = {
        'reservations': reservations,
    }
    return render(request, '3adminrequestconfirmation.html', context)

# 従業員スケジュール一覧画面
def adminemployeeschedulelist(request):
    schedules = EmployeeSchedule.objects.all().order_by('date', 'start_time')
    context = {
        'schedules': schedules,
    }
    return render(request, '3adminemployeeschedulelist.html', context)

# 依頼スケジュール画面
def administratorrequestschedulechange(request):
    return render(request, '3administratorrequestschedulechange.html')

# 管理者従業員一覧画面
def administratorrequestscheduleconfirmation(request):
    return render(request, '3administratorrequestscheduleconfirmation.html')