from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from shop.models.product_model import ProductModel
from customer.models.cart_model import CartModel


class CartItemModel(DateTimeModel):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "cart item"
        verbose_name_plural = "cart items"
