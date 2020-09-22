# Generated by Django 3.1 on 2020-09-01 13:26

from decimal import Decimal
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0007_specification_docdatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='cost',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='RUB', max_digits=19),
        ),
        migrations.AlterField(
            model_name='specification',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='specification',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]