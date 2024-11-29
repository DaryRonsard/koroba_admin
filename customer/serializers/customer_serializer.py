from customer.models.customer_model import CustomerModel
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ['id', 'username', 'phone_number', 'whatsapp_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['user_type'] = 'customer'
        password = validated_data.pop('password', None)
        customer = super().create(validated_data)
        if password:
            customer.set_password(password)
            customer.save()
        return customer
        
    def update(self, instance, validated_data):
        validated_data['user_type'] = 'customer'
        password = validated_data.pop('password', None)
        customer = super().update(instance, validated_data)
        if password:
            customer.set_password(password)
            customer.save()
        return customer
