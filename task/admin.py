from django.contrib import admin
from .models import ScheduledEmail, Book , Member , Borrow

admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Borrow)


class ScheduledEmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'to_email', 'scheduled_time','user')
    search_fields = ('subject', 'to_email')
    list_filter = ('user', 'scheduled_time')

admin.site.register(ScheduledEmail, ScheduledEmailAdmin)