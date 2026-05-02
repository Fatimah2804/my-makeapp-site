from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'service']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'الاسم | שם'}),
            'phone': forms.TextInput(attrs={'placeholder': 'رقم الهاتف | טלפון'}),
        }