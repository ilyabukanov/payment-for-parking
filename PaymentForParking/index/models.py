from django.db import models
from django.core.exceptions import ValidationError
import re
#Модель парковки
class Parking(models.Model):
    adress = models.CharField(max_length=150, verbose_name='Адрес')
    starttime = models.TimeField(auto_now=False, auto_now_add=False,null=True, verbose_name='Время начала работы')
    endtime = models.TimeField(auto_now=False, auto_now_add=False,null=True,verbose_name='Время конца работы')
    minimaltimeforpayment = models.CharField(max_length=50, verbose_name='Минимальное время для оплаты')
    price = models.IntegerField(verbose_name='Цена')
    numberofavailableseats = models.IntegerField(verbose_name='Количество свободных мест', default=0)
    tickets = models.ManyToManyField('tickets', blank=True, verbose_name='Абонементы')
    videofromthecamera = models.CharField(max_length=500, blank=True, verbose_name='Видеоизображение с камеры')

    def __str__(self):
        return self.adress

    class Meta:
        verbose_name = 'Парковка'
        verbose_name_plural = 'Парковки'

#Модель абонемента
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

#Модель оплаченной парковки
class paidparking(models.Model):
    adress = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, verbose_name='Адрес парковки')
    carnumber = models.CharField(max_length=150,verbose_name='Номер автомобиля')
    amountoftime = models.IntegerField(verbose_name='Количество времени')
    price = models.FloatField(verbose_name='Цена')
    telephone = models.CharField(max_length=20,verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронный адрес',null=True,blank=True )
    datetimepaidparking = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время оплаты')
    expirationdate = models.DateField(null=True,verbose_name='Дата начала срока действия')
    expirationtime = models.TimeField(null=True,verbose_name='Время начала срока действия')
    enddateandtime = models.DateTimeField(null=True,blank=True,verbose_name='Окончание срока действия')


    class Meta:
        verbose_name = 'Оплаченная парковка'
        verbose_name_plural = 'Оплаченные парковки'

#Модель оплаченного абонемента
class paidseasontickets(models.Model):
    nametickets = models.ForeignKey(tickets, on_delete=models.SET_NULL, null=True, verbose_name='Наименование абонемента')
    carnumber = models.CharField(max_length=150,verbose_name='Номер автомобиля')
    price = models.FloatField(verbose_name='Цена')
    telephone = models.CharField(max_length=20,verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронный адрес',null=True,blank=True)
    datetimepaidtickets = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время оплаты")
    expirationdate = models.DateField(null=True,verbose_name='Дата начала срока действия')
    expirationtime = models.TimeField(null=True,verbose_name='Время начала срока действия')
    enddateandtime = models.DateTimeField(null=True,blank=True,verbose_name='Окончание срока действия')

    class Meta:
        verbose_name = 'Оплаченный абонемент'
        verbose_name_plural = 'Оплаченные абонементы'

#Модель пользователей telegram
class users(models.Model):
    user_id = models.CharField(max_length=150,verbose_name='ID пользователя')
    phonenumber = models.CharField(max_length=150,verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Пользователи telegram'
        verbose_name_plural = 'Пользователи telegram'




