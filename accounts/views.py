from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, ScheduledEmailForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from task.models import ScheduledEmail
from django.http import Http404
from task.tasks import send_scheduled_email

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "ثبت‌نام با موفقیت انجام شد!")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'accounts/sign_up.html', {'form': form})
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "نام کاربری یا رمز عبور صحیح نیست.")
        else:
            form.add_error(None, "نام کاربری یا رمز عبور صحیح نیست.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

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

def send_email(request):
    if request.method == 'POST':
        form = ScheduledEmailForm(request.POST)
        if form.is_valid():
            scheduled_email = form.save(commit=False)
            scheduled_email.user = request.user
            scheduled_email.save()

            send_scheduled_email.apply_async(
                args=[scheduled_email.id],
                eta=scheduled_email.scheduled_time  
            )

            return redirect('success')
    else:
        form = ScheduledEmailForm()
    
    return render(request, 'send_email.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')
