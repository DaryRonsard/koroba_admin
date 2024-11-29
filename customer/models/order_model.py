from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from customer.models.customer_model import CustomerModel
from shop.models.product_model import ProductModel
from customer.models.cart_model import CartModel

class OrderModel(DateTimeModel):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('in_progress', 'En cours'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée'),
    ]
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'Order {self.id} - {self.status}'