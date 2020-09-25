from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField


class Car(models.Model):
    """Модель автомобиля"""
    class Meta:
        default_permissions = ()
        permissions = [
            ('add_car', 'Добавление автомобиля'),
            ('view_car', 'Просмотр автомобиля'),
            ('change_car', 'Редактирование автомобиля'),
            ('delete_car', 'Удаления автомобиля'),

            ('view_other_car', 'Просмотр чужого автомобиля'),
            ('change_other_car', 'Редактирование чужого автомобиля'),
            ('delete_other_car', 'Удаление чужого автомобиля'),
        ]
        verbose_name = 'Машина'
        verbose_name_plural = "Машины"
        ordering = ['reg_number']

    reg_number = models.CharField(
        max_length=32, unique=True,
        validators=[
            # Регулярное выражение на гос. номер
            RegexValidator(
                '^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}$',
                message=(
                    'Регистрационный номер не соответствует формату: \'аХХХааХХ\' или '
                    '\'аХХХааХХХ\', где \'а\' - буквы русского алфавита, \'Х\' - цифры.'
                )
            ),
        ],
        verbose_name='государственный регистрационный номер'
    )
    model = models.CharField(max_length=64)
    load_capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.model


class AutoPart(models.Model):
    """Автозапчасти и услуги"""
    name = models.CharField(max_length=80)
    partsNumber = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    price = MoneyField(max_digits=19, decimal_places=2, default_currency='RUB')

    def __str__(self):
        return f'{self.name}'

class Specification(models.Model):
    """Спецификация техобслуживания"""
    name = models.CharField(max_length=80, unique=True)
    docDateTime = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200, default='', blank=True)
    cost = MoneyField(max_digits=19, decimal_places=2, default_currency='RUB', default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class SpecificationTable(models.Model):
    """Таблица компонентов спецификации"""
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    autoPart = models.ForeignKey(AutoPart, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=3)
    price = MoneyField(max_digits=19, decimal_places=2, default_currency='RUB')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.specification.name


class Unit(models.Model):
    class Meta:
        ordering=['name']

    name = models.CharField(max_length=10)
    multiple = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name


class FuelType(models.Model):
    name = models.CharField(max_length=20)
    altName = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class FuelNorm(models.Model):
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    fuelType = models.ForeignKey(FuelType, on_delete=models.CASCADE, related_name='fuelType')
    fuelTypeB = models.ForeignKey(FuelType, on_delete=models.CASCADE, related_name='fuelTypeB', null=True)
    fuelTypeC = models.ForeignKey(FuelType, on_delete=models.CASCADE, related_name='fuelTypeC', default=1)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='fuelType', null=True, blank=True)

    def __str__(self):
        return self.fuelType.altName

    class Meta:
        ordering = ['unit']










