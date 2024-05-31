from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from datetime import datetime 

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'



# class PurchaseOrderSerializer(serializers.ModelSerializer):
#     def validate_order_date(self, value):
#         try:
#             datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
#         except ValueError:
#             raise serializers.ValidationError("Order date must be in the format YYYY-MM-DDThh:mm:ssZ.")
#         return value

#     def validate_delivery_date(self, value):
#         try:
#             datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
#         except ValueError:
#             raise serializers.ValidationError("Delivery date must be in the format YYYY-MM-DDThh:mm:ssZ.")
#         return value

#     def validate_quantity(self, value):
#         if not isinstance(value, int):
#             raise serializers.ValidationError("Quantity must be a valid integer.")
#         return value

#     class Meta:
#         model = PurchaseOrder
#         fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
