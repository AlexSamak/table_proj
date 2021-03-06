# Generated by Django 3.1 on 2020-09-01 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('altName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FuelNorm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fuelType', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='specification.fueltype')),
            ],
        ),
    ]
