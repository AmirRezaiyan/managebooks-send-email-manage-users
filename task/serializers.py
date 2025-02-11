from rest_framework import serializers
from .models import Book, Member, Borrow , ScheduledEmail

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'

class ScheduledEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledEmail
        fields = ['id', 'user', 'to_email', 'subject', 'message', 'scheduled_time']
        read_only_fields = ['user']