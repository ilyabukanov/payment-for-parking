# Generated by Django 3.1.5 on 2021-05-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0024_auto_20210429_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='videofromthecamera',
            field=models.CharField(blank=True, max_length=500, verbose_name='Адрес'),
        ),
    ]
