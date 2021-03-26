from django import forms
from  .models import paidparking,paidseasontickets
from django.core.exceptions import ValidationError
import re

class paidparkingForm(forms.ModelForm):
  class Meta:
      model = paidparking
      fields = ['adress','carnumber','amountoftime', 'price', 'email','telephone','expirationdate','expirationtime','enddateandtime']
      widgets = {
          'adress': forms.Select(attrs={"class": "form-control form", "id": "exampleFormControlSelect1"}),
          'carnumber': forms.TextInput(attrs={"class": "form-control form-control-lg form"}),
          'amountoftime': forms.NumberInput(attrs={"class": "number form-control form-control-lg form"}),
          'price': forms.NumberInput(attrs={"class": "form-control form-control-lg form", "readonly": 0}),
          'email': forms.EmailInput(attrs={"class": "form-control form-control-lg form"}),
          'telephone': forms.TextInput(attrs={"class": "form-control form-control-lg form"}),
          'expirationdate': forms.DateInput(attrs={"type": "date","class": "form form-control form-control-lg", "disabled": 1}),
          'expirationtime': forms.TimeInput(attrs={"type": "time", "class": "form form-control form-control-lg", "disabled": 1}),
          'enddateandtime':  forms.TextInput(attrs={"class": "form form-control form-control-lg", "readonly": 0}),
      }
  def clean_telephone(self):
      telephone = self.cleaned_data['telephone']
      if not re.match('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', telephone):
          raise forms.ValidationError('Номер телефона введён не верно')
      return telephone

  def clean_carnumber(self):
        carnumber = self.cleaned_data['carnumber']
        r = re.compile('[А-Я]\d{3}[А-Я]{2}\d{2,3}')
        if r.search(carnumber):
            pass
        else:
            raise ValidationError('Номер автомобиля введён не верно')
        return carnumber

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

   def clean_telephone(self):
       telephone = self.cleaned_data['telephone']
       # r = re.compile('^\+7|8\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}')
       if not re.match('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', telephone):
           raise ValidationError('Номер телефона введён не верно')
       return telephone

   def clean_carnumber(self):
       carnumber = self.cleaned_data['carnumber']
       r = re.compile('[А-Я]\d{3}[А-Я]{2}\d{2,3}')
       if r.search(carnumber):
           pass
       else:
           raise ValidationError('Номер автомобиля введён не верно')
       return carnumber
