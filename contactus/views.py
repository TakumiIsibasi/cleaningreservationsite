from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactUsForm

# お問い合わせ画面
class ContactUsCreateView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, "contactus/2contactus.html", {"form": form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # 保存する
            form.save()
            # メール送信
            try:
                send_mail(
                    subject="お問い合わせがありました",
                    message=f"名前: {form.cleaned_data['contactus_name']}\n"
                            f"メールアドレス: {form.cleaned_data['contactus_email']}\n"
                            f"メッセージ: {form.cleaned_data['contactus_message']}",
                    from_email=None,  # settings.DEFAULT_FROM_EMAILが使われます
                    recipient_list=["fko2347076@stu.o-hara.ac.jp"],  # 管理者のメールアドレス
                )
            except BadHeaderError:
                return HttpResponse("無効なヘッダーが検出されました。")
            
            return redirect("contactus:submissioncomplete")
        return render(request, "contactus/2contactus.html", {"form": form})

# お問い合わせ送信完了画面
def submissioncomplete(request):
    return render(request, "contactus/2submissioncomplete.html")
