from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactusForm


# お問い合わせ画面
class ContactusCreateView(View):
    def get(self, request):
        form = ContactusForm()
        return render(request, "contactus/2contactus.html", {"form": form})
    
    def post(self, request):
        form = ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contactus:submissioncomplete")
        return render(request, "contactus/2contactus.html", {"form": form})

# お問い合わせ送信完了画面
def submissioncomplete(request):
    return render(request, 'contactus/2submissioncomplete.html')

contactus_create = ContactusCreateView.as_view()