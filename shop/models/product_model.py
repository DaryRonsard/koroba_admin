from django.db import models
from base.models.helpers.date_time_model import DateTimeModel
from shop.models.artisan_model import ArtisanModel
from django.contrib.auth.models import Group, Permission

class ProductModel(DateTimeModel):
    artisan = models.ForeignKey(ArtisanModel, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=500)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_picture = models.URLField(max_length=200, blank=True, null=True)

#Il permet d'avoir la liste de tous les utilisateurs
    groups = models.ManyToManyField(
        Group,
        related_name='product_users',  
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='product_permissions',  
        blank=True
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name
