# Generated by Django 3.1.5 on 2021-02-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20210201_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
