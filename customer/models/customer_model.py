from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from accounts.models import UserModel


class CustomerModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='customer_profile')
    groups = models.ManyToManyField(
        Group,
        related_name='customer_users',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_permissions',  
        blank=True
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.username
