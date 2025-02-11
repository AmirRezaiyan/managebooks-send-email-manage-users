from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import ScheduledEmail

@shared_task
def send_scheduled_email(email_id):
    try:
        email = ScheduledEmail.objects.get(id=email_id)
        send_mail(
            email.subject,
            email.message,
            settings.DEFAULT_FROM_EMAIL,
            [email.to_email],
            fail_silently=False,
        )
        email.status = 'sent'
        email.save()
        return f"Email sent to {email.to_email}"
    except ScheduledEmail.DoesNotExist:
        return "Email not found."