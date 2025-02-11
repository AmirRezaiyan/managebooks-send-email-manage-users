from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser  
from task.models import ScheduledEmail
from django.utils import timezone

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلاً استفاده شده است.")
        return email

class ScheduledEmailForm(forms.ModelForm):
    class Meta:
        model = ScheduledEmail
        fields = ['subject', 'message', 'to_email', 'scheduled_time']
    
    def clean_scheduled_time(self):
        send_time = self.cleaned_data.get('scheduled_time')
        if send_time < timezone.now():
            raise forms.ValidationError("زمان ارسال باید در آینده باشد.")
        return send_time

class SendEmailForm(forms.Form):
    to_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=500)