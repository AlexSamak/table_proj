# Generated by Django 3.1 on 2020-09-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specification', '0005_auto_20200901_0710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='unit',
            name='description',
            field=models.CharField(default='', max_length=30),
        ),
    ]
