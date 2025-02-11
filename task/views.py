from rest_framework import viewsets
from .models import Book, Member, Borrow , ScheduledEmail
from .serializers import BookSerializer, MemberSerializer, BorrowSerializer , ScheduledEmailSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render , redirect
from .tasks import send_scheduled_email
from .forms import ScheduledEmailForm
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

class ScheduledEmailViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduledEmailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ScheduledEmail.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def home(request):
    return render(request, 'home.html')


def schedule_email_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        to_email = request.POST.get('to_email')
        scheduled_time = request.POST.get('scheduled_time')

        email = ScheduledEmail.objects.create(
            subject=subject,
            message=message,
            to_email=to_email,
            scheduled_time=scheduled_time,
        )

        send_scheduled_email.apply_async((email.id,), eta=scheduled_time)

        return redirect('dashboard')

    return render(request, 'schedule_email.html')

def scheduled_email_list(request):
    emails = ScheduledEmail.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'scheduled_email_list.html', {'scheduled_emails': emails})

def scheduled_email_edit(request, email_id):
    email_obj = get_object_or_404(ScheduledEmail, id=email_id, user=request.user)

    if request.method == 'POST':
        form = ScheduledEmailForm(request.POST, instance=email_obj)
        if form.is_valid():
            form.save()
            return redirect('scheduled_email_list')
    else:
        form = ScheduledEmailForm(instance=email_obj)

    return render(request, 'scheduled_email_edit.html', {'form': form})

def scheduled_email_delete(request, email_id):
    email = get_object_or_404(ScheduledEmail, id=email_id, user=request.user)
    email.delete()
    return redirect('scheduled_email_list')

def dashboard_view(request):
    emails = ScheduledEmail.objects.all().order_by('-created_at')
    return render(request, 'dashboard.html', {'emails': emails})
