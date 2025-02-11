from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrows')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrows')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
    
class ScheduledEmail(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    to_email = models.EmailField()
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return f"{self.subject} - {self.to_email}"