from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from customer.models.order_model import OrderModel
from shop.models.product_model import ProductModel
from shop.models.artisan_model import ArtisanModel

class OrderItemModel(DateTimeModel):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    artisan = models.ForeignKey(ArtisanModel, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Order item"
        verbose_name_plural = "Order items"

    def __str__(self):
        return f'OrderItem {self.id} - {self.product.name}'