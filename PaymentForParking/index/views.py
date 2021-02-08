from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import paidparkingForm,paidseasonticketsForm
from django.template import RequestContext
from .models import Parking,paidparking,paidseasontickets,tickets
from django.http import JsonResponse
import json
from sendsms.message import SmsMessage

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
        return JsonResponse({'price': seasontickets.price})
    else:
        pass

def paymenttickets(request):
    if request.method == 'POST':
        #Получение данных, связанных с моделью
        formtickets = paidseasonticketsForm(request.POST)
        #Если валидация пройдена
        if formtickets.is_valid():
            #form.cleaned_data - словарь, который содержит в себе все поля после отправки формы
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
    return render(request, 'index/personalaccount.html',
                  {'paymentparking': paymentparking, 'paymenttickets': paymenttickets})
