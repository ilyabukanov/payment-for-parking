# Generated by Django 3.1.5 on 2021-01-20 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameseasontickets', models.CharField(db_index=True, max_length=150, verbose_name='Наименование')),
                ('numberofdays', models.CharField(max_length=50, verbose_name='Количество дней')),
                ('time', models.CharField(max_length=50, verbose_name='Период времени')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Парковка',
                'verbose_name_plural': 'Парковки',
            },
        ),
        migrations.AddField(
            model_name='parking',
            name='tickets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='index.tickets', verbose_name='Абонемент'),
        ),
    ]
