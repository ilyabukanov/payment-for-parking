from django import forms
from  .models import paidparking,paidseasontickets
import re
from django.core.exceptions import ValidationError

class paidparkingForm(forms.ModelForm):
  class Meta:
      model = paidparking
      fields = ['adress','carnumber','amountoftime', 'price', 'telephone']
      widgets = {
          'adress': forms.Select(attrs={"class": "form-control", "id": "exampleFormControlSelect1"}),
          'carnumber': forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Формат: x111xx177"}),
          'amountoftime': forms.NumberInput(attrs={"class": "number form-control form-control-lg"}),
          'price': forms.NumberInput(attrs={"class": "form-control form-control-lg", "readonly": 0}),
          'telephone': forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "89152021645"}),
      }

class paidseasonticketsForm(forms.ModelForm):
   class Meta:
              model = paidseasontickets
              fields = ['nametickets','carnumber', 'price', 'telephone']
              widgets = {
                  'nametickets': forms.Select(attrs={"class": "form-control", "id": "exampleFormControlSelect1"}),
                  'carnumber': forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Формат: x111xx177"}),
                  'price': forms.NumberInput(attrs={"class": "form-control form-control-lg", "readonly": 0}),
                  'telephone': forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "89152021645"}),
              }
#Кастомный валидатор на проверку телефона
  #def clean_telephone(self):
   #   telephone = self.cleaned_data['telephone']
    #  if re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', telephone):
     #     raise ValidationError('Телефон должен иметь формат 89152021645')
      #return telephone