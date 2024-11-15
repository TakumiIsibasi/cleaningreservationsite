from django.shortcuts import render

# 管理者ホーム画面
def adminhome(request):
    return render(request, '3adminhome.html')

# 管理者従業員一覧画面
def adminemployeelist(request):
    return render(request, '3adminemployeelist.html')

# 依頼管理画面
def adminrequestconfirmation(request):
    return render(request, '3adminrequestconfirmation.html')

# 従業員スケジュール一覧画面
def adminemployeeschedulelist(request):
    return render(request, '3adminemployeeschedulelist.html')

# 依頼スケジュール画面
def administratorrequestschedulechange(request):
    return render(request, '3administratorrequestschedulechange.html')

# 管理者従業員一覧画面
def administratorrequestscheduleconfirmation(request):
    return render(request, '3administratorrequestscheduleconfirmation.html')