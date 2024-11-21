from django.shortcuts import render

# 従業員ホーム
def employeehome(request):
    return render(request, '4employeehome.html')

# 従業員スケジュールメニュー
def employeescheduleconfirmation(request):
    return render(request, '4employeescheduleconfirmation.html')

# 清掃依頼確認
def employeereservationconfirmation(request):
    return render(request, '4employeereservationconfirmation.html')

# 清掃依頼詳細確認
def reservationdetailsconfirmation(request):
    return render(request, '4reservationdetailsconfirmation.html')

# スケジュール追加
def employeescheduleaddition(request):
    return render(request, '4employeescheduleaddition.html')

# スケジュール変更
def employeeschedulechange(request):
    return render(request, '4employeeschedulechange')

# スケジュール削除
def employeescheduledeletion(request):
    return render(request, '4employeescheduledeletion.html')
