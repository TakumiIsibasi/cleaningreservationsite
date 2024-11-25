from django import forms
from .models import EmployeeSchedule

class EmployeeScheduleForm(forms.ModelForm):
    class Meta:
        model = EmployeeSchedule
        fields = ['date', 'start_time', 'end_time', 'task']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'task': forms.TextInput(attrs={'class': 'form-control'}),
        }
