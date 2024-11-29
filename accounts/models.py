from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models.helpers.date_time_model import DateTimeModel

class UserModel(AbstractUser, DateTimeModel):
    USER_TYPES = [
        ('artisan', 'Artisan'),
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    ]
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='customer')
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username