# Generated by Django 3.1.5 on 2021-02-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20210201_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='price',
            field=models.IntegerField(blank=True, verbose_name='Цена'),
        ),
    ]
