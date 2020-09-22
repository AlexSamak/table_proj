from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

#API
router.register('cars', views.CarViewSet)
router.register('autoParts', views.AutoPartViewSet)
router.register('specifications', views.SpecificationViewSet)
router.register('specificationTables', views.SpecificationViewSet)
router.register('units', views.UnitViewSet)
router.register('fuelTypes', views.FuelTypeViewSet)
router.register('fuelNorms', views.FuelNormViewSet)

urlpatterns = router.urls
