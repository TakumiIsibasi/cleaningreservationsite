from django.shortcuts import render

# Create your views here.

# お問い合わせ画面
def contactus(request):
    return render(request, '2contactus.html')

# お問い合わせ送信完了画面
def submissioncomplete(request):
    return render(request, '2submissioncomplete.html')