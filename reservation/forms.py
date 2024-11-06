from django import forms
from .models import user_reservation

class UserForm(forms.ModelForm):
    class Meta:
        model = user_reservation
        fields = ["user_name", "user_phone", "user_email", "user_address",
                  "user_cleaning_location", "user_cleaning_date", "user_comments"]
