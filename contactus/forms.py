from django.forms import ModelForm
from .models import User_contactus
 
class ContactusForm(ModelForm):
    class Meta:
        model = User_contactus
        fields = ["contactus_name", "contactus_email", "contactus_message"]