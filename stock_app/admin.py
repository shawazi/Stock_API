from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register((Category, Brand, Firm, Product, Sale, Purchase))