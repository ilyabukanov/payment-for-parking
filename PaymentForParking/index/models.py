from django.db import models
from django.core.exceptions import ValidationError
import re
class Parking(models.Model):
    adress = models.CharField(max_length=150, verbose_name='Адрес')
    workinghours = models.CharField(max_length=50, verbose_name='Время работы')
    minimaltimeforpayment = models.CharField(max_length=50, verbose_name='Минимальное время для оплаты')
    price = models.IntegerField(verbose_name='Цена')
    numberofavailableseats = models.IntegerField(verbose_name='Количество свободных мест', default=0)
    tickets = models.ManyToManyField('tickets', blank=True, verbose_name='Абонементы')

    def __str__(self):
        return self.adress

    class Meta:
        verbose_name = 'Парковка'
        verbose_name_plural = 'Парковки'

class tickets(models.Model):
            nameseasontickets = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
            numberofdays = models.CharField(max_length=50, verbose_name='Количество дней')
            time = models.CharField(max_length=50, verbose_name='Период времени')
            price = models.IntegerField(verbose_name='Цена')

            def __str__(self):
                return self.nameseasontickets

            class Meta:
                verbose_name = 'Абонемент'
                verbose_name_plural = 'Абонементы'


class paidparking(models.Model):
    adress = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, verbose_name='Адрес парковки')
    carnumber = models.CharField(max_length=150,verbose_name='Номер автомобиля')
    amountoftime = models.IntegerField(verbose_name='Количество времени')
    price = models.FloatField(verbose_name='Цена')
    telephone = models.CharField(max_length=20,verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронный адрес',null=True,blank=True )
    datetimepaidparking = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время оплаты')
    startofvalidityperiod = models.DateTimeField(null=True,verbose_name='Начало срока действия')
    expirationdate = models.DateTimeField(null=True,blank=True,verbose_name='Окончание срока действия')


    class Meta:
        verbose_name = 'Оплаченная парковка'
        verbose_name_plural = 'Оплаченные парковки'

class paidseasontickets(models.Model):
    nametickets = models.ForeignKey(tickets, on_delete=models.SET_NULL, null=True, verbose_name='Наименование абонемента')
    carnumber = models.CharField(max_length=150,verbose_name='Номер автомобиля')
    price = models.FloatField(verbose_name='Цена')
    telephone = models.CharField(max_length=20,verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронный адрес',null=True,blank=True)
    datetimepaidtickets = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время оплаты")
    startofvalidityperiod = models.DateTimeField(null=True,verbose_name='Начало срока действия')
    expirationdate = models.DateTimeField(null=True,blank=True,verbose_name='Окончание срока действия')

    class Meta:
        verbose_name = 'Оплаченный абонемент'
        verbose_name_plural = 'Оплаченные абонементы'




