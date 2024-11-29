from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from customer.models.customer_model import CustomerModel
from shop.models.product_model import ProductModel



class CartModel(DateTimeModel):
    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE, related_name='cart')
    quantity = models.CharField(max_length=15)
    # product_picture = models.URLField(max_length=500, blank=True, null=True)



    class Meta:
        verbose_name = "cart"
        verbose_name_plural = "carts"


      







    
    


