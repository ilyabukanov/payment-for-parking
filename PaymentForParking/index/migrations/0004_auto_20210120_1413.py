# Generated by Django 3.1.5 on 2021-01-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20210120_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='numberofavailableseats',
            field=models.IntegerField(default=0, verbose_name='Количество свободных мест'),
        ),
        migrations.AlterField(
            model_name='parking',
            name='tickets',
            field=models.ManyToManyField(blank=True, to='index.tickets', verbose_name='Абонементы'),
        ),
    ]
