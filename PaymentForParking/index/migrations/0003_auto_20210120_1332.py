# Generated by Django 3.1.5 on 2021-01-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20210120_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tickets',
            options={'verbose_name': 'Абонемент', 'verbose_name_plural': 'Абонементы'},
        ),
        migrations.RemoveField(
            model_name='parking',
            name='tickets',
        ),
        migrations.AddField(
            model_name='parking',
            name='tickets',
            field=models.ManyToManyField(blank=True, to='index.tickets'),
        ),
    ]