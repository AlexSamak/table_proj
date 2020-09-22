from django.contrib import admin

from .models import Specification, SpecificationTable, AutoPart, Car, FuelType, FuelNorm, Unit

admin.site.register(Specification)
admin.site.register(SpecificationTable)
admin.site.register(AutoPart)
admin.site.register(Car)
# admin.site.register(FuelType)
# admin.site.register(FuelNorm)
admin.site.register(Unit)

@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'altName')


@admin.register(FuelNorm)
class FuelNormAdmin(admin.ModelAdmin):
    list_display = ('fuelType', 'fuelTypeB', 'fuelTypeC', 'quantity', 'unit')
