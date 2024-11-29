from django.contrib import admin


from customer.models.cart_model import CartModel
from customer.models.order_model import OrderModel
from customer.models.orderItem_model import OrderItemModel
from customer.models.cartsItem_models import CartItemModel
from core_admin.admin import admin_site




@admin.register(CartModel, site=admin_site)
class CartAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product', 'created_at')
    search_fields = ('quantity', 'created_at')
    search_fields = ('id', 'customer')




@admin.register(OrderModel, site=admin_site)
class OrderAdmin(admin.ModelAdmin):
    #fields = ('customer', 'status','total_amount', 'commission_amount')
    list_display = ('customer', 'status','total_amount', 'commission_amount')
    search_fields = ('id', 'customer')
    #exclude = ('created_at',)


@admin.register(OrderItemModel, site=admin_site)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ('id', 'order', 'product', 'quantity', 'price')


@admin.register(CartItemModel, site=admin_site)
class CardItemAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product', 'cart', 'created_at')
    search_fields = ('quantity', 'product')


