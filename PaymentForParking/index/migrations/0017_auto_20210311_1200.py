# Generated by Django 3.1.5 on 2021-03-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_paidseasontickets_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidparking',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронный адрес'),
        ),
        migrations.AlterField(
            model_name='paidseasontickets',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронный адрес'),
        ),
    ]
