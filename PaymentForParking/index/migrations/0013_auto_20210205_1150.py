# Generated by Django 3.1.5 on 2021-02-05 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20210201_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidparking',
            name='datetimepaidparking',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 2, 5, 11, 50, 19, 711634, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paidseasontickets',
            name='datetimepaidtickets',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 2, 5, 11, 50, 22, 318834, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
