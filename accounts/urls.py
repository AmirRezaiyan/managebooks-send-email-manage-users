from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('send-email/', views.send_email, name='send_email'),
    path('success/', views.success_page, name='success'),
]
