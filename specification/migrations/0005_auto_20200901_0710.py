# Generated by Django 3.1 on 2020-09-01 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0004_fuelnorm_fueltypec'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('multiple', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='fuelnorm',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuelType', to='specification.unit'),
        ),
    ]