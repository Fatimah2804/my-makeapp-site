from django.db import models
from django.db import models

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('evening', 'Evening Makeup | مكياج سهرة'),
        ('bridal', 'Bridal Makeup | مكياج عروس'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
# Create your models here.
