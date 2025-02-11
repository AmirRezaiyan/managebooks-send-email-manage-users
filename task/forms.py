from django import forms
from .models import ScheduledEmail
from django.utils import timezone

class ScheduledEmailForm(forms.ModelForm):
    class Meta:
        model = ScheduledEmail
        fields = ['subject', 'message', 'to_email', 'scheduled_time']
    
    def clean_scheduled_time(self):
        scheduled_time = self.cleaned_data.get('scheduled_time')
        if scheduled_time < timezone.now():
            raise forms.ValidationError("زمان ارسال باید در آینده باشد.")
        return scheduled_time
