# Generated by Django 3.1.5 on 2021-04-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_auto_20210422_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=150, verbose_name='ID пользователя')),
                ('phonenumber', models.CharField(max_length=150, verbose_name='Номер телефона')),
            ],
        ),
    ]