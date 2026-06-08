from django.urls import path
from .views import book_appointment, success_page, weekly_schedule
from . import views

urlpatterns = [
    path('book/', book_appointment, name='book_appointment'),
    path('success/', success_page, name='success'),
    path('schedule/', weekly_schedule, name='weekly_schedule'),
    
]