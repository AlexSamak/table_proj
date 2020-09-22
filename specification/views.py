from rest_framework import viewsets
from specification.serializers import *
from specification.filters import *

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class AutoPartViewSet(viewsets.ModelViewSet):
    queryset = AutoPart.objects.all()
    serializer_class = AutoPartSerializer


class SpecificationViewSet(viewsets.ModelViewSet):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer


class SpecificationTableViewSet(viewsets.ModelViewSet):
    queryset = SpecificationTable.objects.all()
    serializer_class = SpecificationTableSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class FuelTypeViewSet(viewsets.ModelViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class FuelNormViewSet(viewsets.ModelViewSet):
    queryset = FuelNorm.objects.all()
    serializer_class = FuelNormSerializer
