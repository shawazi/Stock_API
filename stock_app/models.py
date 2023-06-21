from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UpdateCreateData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
class Category(UpdateCreateData):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Brand(UpdateCreateData):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="brands", default="default.png", null=True, blank=True)

    
    def __str__(self):
        return self.name

class Product(UpdateCreateData):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    stock = models.IntegerField(blank=True, default=0)

    
    def __str__(self):
        return f"{self.category} - {self.brand} - {self.name} --> {self.stock}"
    
class Firm(UpdateCreateData):
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    image = models.ImageField(upload_to="firms", default="default.png", null=True, blank=True)

    def __str__(self):
        return self.name
    
class Purchase(UpdateCreateData):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    firm = models.ForeignKey(Firm, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity} - {self.price}"
    
    @property
    def price_total(self):
        return self.quantity * self.price
    
class Sale(UpdateCreateData):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity} - {self.price}"
    
    @property
    def price_total(self):
        return self.quantity * self.price