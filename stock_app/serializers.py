from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
class CategoryProductSerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # products = serializers.StringRelatedField(many=True, read_only=True)

    products = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = "__all__"
        
class FirmSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Firm
        fields = "__all__"
        
class PurchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Purchase
        fields = "__all__"
        
class SaleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sale
        fields = "__all__"
        
    def validate(self, data):
        product = data.get("product")
        quantity = data.get("quantity")
        
        if quantity > product.stock:
            raise serializers.ValidationError({"quantity": "Insufficient stock available for this sale."})
        return super().validate(data)