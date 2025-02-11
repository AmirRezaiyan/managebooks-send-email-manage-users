from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet, BorrowViewSet , ScheduledEmailViewSet , home
from .views import schedule_email_view, dashboard_view 
from .views import scheduled_email_list, scheduled_email_edit, scheduled_email_delete

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'members', MemberViewSet, basename='member')
router.register(r'borrows', BorrowViewSet, basename='borrow')
router.register(r'scheduled-emails', ScheduledEmailViewSet, basename='scheduled-email')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', home, name='home'),
    path('schedule-email/', schedule_email_view, name='schedule_email'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('scheduled-emails/', scheduled_email_list, name='scheduled_email_list'),
    path('scheduled-emails/edit/<int:email_id>/', scheduled_email_edit, name='scheduled_email_edit'),
    path('scheduled-emails/delete/<int:email_id>/', scheduled_email_delete, name='scheduled_email_delete'),
]
