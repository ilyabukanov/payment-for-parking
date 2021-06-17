from django import forms
from  .models import paidparking,paidseasontickets
from django.core.exceptions import ValidationError
import re
from .models import Parking,paidparking,paidseasontickets,tickets
from datetime import datetime, timedelta
from datetime import datetime
from datetime import time
#Форма оплаты парковок
class paidparkingForm(forms.ModelForm):
  class Meta:
      model = paidparking
      fields = ['adress','carnumber','amountoftime', 'price', 'email','telephone','expirationdate','expirationtime','enddateandtime']
      widgets = {
          'adress': forms.Select(attrs={"class": "form-control form", "id": "exampleFormControlSelect1"}),
          'carnumber': forms.TextInput(attrs={"class": "form-control form-control-lg form"}),
          'amountoftime': forms.NumberInput(attrs={"class": "number form-control form-control-lg form", "disabled": 1}),
          'price': forms.NumberInput(attrs={"class": "form-control form-control-lg form", "readonly": 0}),
          'email': forms.EmailInput(attrs={"class": "form-control form-control-lg form"}),
          'telephone': forms.TextInput(attrs={"class": "form-control form-control-lg form"}),
          'expirationdate': forms.DateInput(attrs={"type": "date","class": "form form-control form-control-lg", "disabled": 1}),
          'expirationtime': forms.TimeInput(attrs={"type": "time", "class": "form form-control form-control-lg", "disabled": 1}),
          'enddateandtime':  forms.TextInput(attrs={"class": "form form-control form-control-lg", "readonly": 0}),
      }
  #Валидация для номера телефона при оплате парковок
  def clean_telephone(self):
      telephone = self.cleaned_data['telephone']
      if not re.match('^((\+7)+([0-9]){10})$', telephone):
          raise forms.ValidationError('Номер телефона введён не верно')
      return telephone
  #Валидация для номера автомобиля при оплате парковок
  def clean_carnumber(self):
        carnumber = self.cleaned_data['carnumber']
        r = re.compile('[А-Я]\d{3}[А-Я]{2}\d{2,3}')
        if r.search(carnumber):
            pass
        else:
            raise ValidationError('Номер автомобиля введён не верно')
        return carnumber
  #Валидация дла времени начала срока действия
  def clean_expirationtime(self):
      time = self.cleaned_data['expirationtime']
      adress = self.cleaned_data['adress']
      parking = Parking.objects.get(adress=adress)
      starttime = parking.starttime
      endtime = parking.endtime
      if starttime < time < endtime:
          pass
      else:
          raise forms.ValidationError('Время выбрано не верно. Парковка не работает.')
      return time

  #Валидация для времени окончания срока действия
  def clean_enddateandtime(self):
      enddateandtime = self.cleaned_data['enddateandtime']
      PATTERN_OUT = "%H:%M"
      date_time = (datetime.strftime(enddateandtime, PATTERN_OUT))
      date_time = time(*map(int, date_time.split(':')))
      adress = self.cleaned_data['adress']
      parking = Parking.objects.get(adress=adress)
      starttime = parking.starttime
      endtime = parking.endtime
      if starttime < date_time < endtime:
          pass
      else:
          raise forms.ValidationError('Выбрано большое количество времени. Время окончания срока дейтсвия оплаты не совпадает с временем работы парковки.')
      return enddateandtime

  #Валидация для цены при оплате парковок
  def clean_price(self):
      price = self.cleaned_data['price']
      adress = self.cleaned_data['adress']
      parking = Parking.objects.get(adress=adress)
      if(price<parking.price):
          raise forms.ValidationError('Цена за парковку указана не верно. '
                                      'Пожалуйста, не изменяйте цену парковки самостоятельно!!!!')
      return price
  #Валидация для минимального времени для оплаты парковок
  def clean_amountoftime(self):
      amountoftime = self.cleaned_data['amountoftime']
      adress = self.cleaned_data['adress']
      parking = Parking.objects.get(adress=adress)
      minimaltimeforpayment = re.sub("\D", "", parking.minimaltimeforpayment)
      if(str(amountoftime)<minimaltimeforpayment):
          raise forms.ValidationError('Минимальное время для оплаты парковки указано не верно. '
                                      'Пожалуйста, не изменяйте минимально время для оплаты парковки самостоятельно!!!!')
      return amountoftime





#Форма оплаты абонементов
class paidseasonticketsForm(forms.ModelForm):
   class Meta:
              model = paidseasontickets
              fields = ['nametickets','carnumber', 'price', 'email', 'telephone', 'expirationdate','expirationtime','enddateandtime']
              widgets = {
                  'nametickets': forms.Select(attrs={"class": "form form-control", "id": "exampleFormControlSelect1"}),
                  'carnumber': forms.TextInput(attrs={"class": "form form-control form-control-lg"}),
                  'price': forms.NumberInput(attrs={"class": "form form-control form-control-lg", "readonly": 0}),
                  'email': forms.EmailInput(attrs={"class": "form form-control form-control-lg"}),
                  'telephone': forms.TextInput(attrs={"class": "form form-control form-control-lg"}),
                  'expirationdate': forms.DateInput(
                      attrs={"type": "date", "class": "form form-control form-control-lg","disabled": 1}),
                  'expirationtime': forms.TimeInput(
                      attrs={"type": "time", "class": "form form-control form-control-lg","disabled": 1}),
                  'enddateandtime':  forms.TextInput(attrs={"class": "form form-control form-control-lg", "readonly": 0}),
              }
   #Валидация номеря телефона при оплате абонементов
   def clean_telephone(self):
       telephone = self.cleaned_data['telephone']
       # r = re.compile('^\+7|8\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}')
       if not re.match('^((\+7)+([0-9]){10})$', telephone):
           raise ValidationError('Номер телефона введён не верно')
       return telephone
   #Валидация номера автомобиля при оплате абонементов
   def clean_carnumber(self):
       carnumber = self.cleaned_data['carnumber']
       r = re.compile('[А-Я]\d{3}[А-Я]{2}\d{2,3}')
       if r.search(carnumber):
           pass
       else:
           raise ValidationError('Номер автомобиля введён не верно')
       return carnumber
   #Валидация цены при оплате абонемента
   def clean_price(self):
       price = self.cleaned_data['price']
       nametickets = self.cleaned_data['nametickets']
       Tickets = tickets.objects.get(nameseasontickets=nametickets)
       if (price<Tickets.price):
           raise forms.ValidationError(
               'Цена за абонемент указана не верно. Пожалуйста, не изменяйте цену абонемента самостоятельно!!!!')
       return price
