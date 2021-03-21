from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import paidparkingForm,paidseasonticketsForm
from django.template import RequestContext
from .models import Parking,paidparking,paidseasontickets,tickets
from django.http import JsonResponse
from django.core.mail import send_mail
import json
from datetime import datetime

def index(request):
    parking = Parking.objects.all()
    return render(request, 'index/index.html', {'parking': parking})

def exit(request):
    if "phonenumber" in request.session:
        del request.session['phonenumber']
    return render(request, 'index/exit.html')

def session(request):
    request.session['phonenumber'] = 'phonenumber'
    return HttpResponse("yes")

def enter(request):
    return render(request, 'index/enter.html')

def pricingplans(request):
    parking = Parking.objects.all()
    return render(request, 'index/pricingplans.html',  {'parking': parking})

def payment(request):
    if request.method == 'POST':
        #Получение данных, связанных с моделью
      formparking = paidparkingForm(request.POST)
        #Если валидация пройдена
      if formparking.is_valid():
            if formparking.cleaned_data['email'] != "":
                adress = formparking.cleaned_data['adress']
                adress = str(adress)

                startofvalidityperiod = formparking.cleaned_data['startofvalidityperiod']
                PATTERN_OUT = "%d.%m.%Y. %H:%M"
                startofvalidityperiod = (datetime.strftime(startofvalidityperiod, PATTERN_OUT))
                startofvalidityperiod = str(startofvalidityperiod)

                expirationdate = formparking.cleaned_data['expirationdate']
                PATTERN_OUT = "%d.%m.%Y. %H:%M"
                expirationdate = (datetime.strftime(expirationdate, PATTERN_OUT))
                expirationdate = str(expirationdate)

                send_mail('Оплата парковки в системе оплаты парковок', "Вас приветствует система оплаты парковок. Вы оплатили парковку по адресу: " + adress + ". Срок действия начинается с " + startofvalidityperiod + " и заканчивается " + expirationdate,'p_i.d.bukanov@mpt.ru',[formparking.cleaned_data['email']])
            #form.cleaned_data - словарь, который содержит в себе все поля после отправки формы
            formparking.save()
            return redirect('home')
    else:
        formparking = paidparkingForm()
    return render(request, 'index/payment.html', {'formparking': formparking})

def valuesubstitution(request):
    if request.method == 'GET':
        adress = request.GET["adress"]
        parking = Parking.objects.get(adress=adress)
        return JsonResponse({'price': parking.price, 'minimaltimeforpayment': parking.minimaltimeforpayment})
    else:
        pass

def seasonticketprice(request):
    if request.method == 'GET':
        nametickets = request.GET["nametickets"]
        seasontickets = tickets.objects.get(nameseasontickets=nametickets)
        return JsonResponse({'price': seasontickets.price, 'numberofdays': seasontickets.numberofdays})
    else:
        pass

def paymenttickets(request):
    if request.method == 'POST':
        #Получение данных, связанных с моделью
        formtickets = paidseasonticketsForm(request.POST)
        #Если валидация пройдена
        if formtickets.is_valid():
            if formtickets.cleaned_data['email'] != "":
                nametickets = formtickets.cleaned_data['nametickets']
                nametickets = str(nametickets)

                startofvalidityperiod = formtickets.cleaned_data['startofvalidityperiod']
                PATTERN_OUT = "%d.%m.%Y. %H:%M"
                startofvalidityperiod = (datetime.strftime(startofvalidityperiod, PATTERN_OUT))
                startofvalidityperiod = str(startofvalidityperiod)

                expirationdate = formtickets.cleaned_data['expirationdate']
                PATTERN_OUT = "%d.%m.%Y. %H:%M"
                expirationdate = (datetime.strftime(expirationdate, PATTERN_OUT))
                expirationdate = str(expirationdate)

                send_mail('Оплата парковки в системе оплаты парковок',
                          "Вас приветствует система оплаты парковок. Вы оплатилиу " + nametickets + ". Срок действия начинается с " + startofvalidityperiod + " и заканчивается " + expirationdate,
                          'p_i.d.bukanov@mpt.ru', [formtickets.cleaned_data['email']])
            formtickets.save()
            return redirect('home')
    else:
        formtickets = paidseasonticketsForm()
    return render(request, 'index/paymenttickets.html', {'formtickets': formtickets})

def personalaccount(request):
    if request.GET:
        phonenumber = request.GET["number"]
        paymentparking = paidparking.objects.filter(telephone=phonenumber)
        paymenttickets = paidseasontickets.objects.filter(telephone=phonenumber)
    else:
        pass
    return render(request, 'index/personalaccount.html', {'paymentparking': paymentparking, 'paymenttickets': paymenttickets})