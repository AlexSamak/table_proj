from rest_framework import serializers
from . import models


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = '__all__'


class AutoPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AutoPart
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specification
        fields = [
            'name',
            'car',
            'docDateTime',
            'description',
            'cost',
        ]


class SpecificationTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SpecificationTable
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = '__all__'


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FuelType
        fields = '__all__'


class FuelNormSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FuelNorm
        fields = '__all__'
