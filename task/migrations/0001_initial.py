# Generated by Django 5.1.5 on 2025-02-01 14:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('inventory', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('membership_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to='task.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrows', to='task.member')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('scheduled_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('sent', 'Sent'), ('failed', 'Failed')], default='pending', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_emails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
