from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("category", CategoryView)
router.register("brand", BrandView)
router.register("firm", FirmView)
router.register("product", ProductView)
router.register("purchase", PurchaseView)
router.register("sale", SaleView)

urlpatterns = [
    
] + router.urls