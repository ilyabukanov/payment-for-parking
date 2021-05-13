from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import paidparkingForm,paidseasonticketsForm
from django.template import RequestContext
from .models import Parking,paidparking,paidseasontickets,tickets,users
from django.http import JsonResponse
from django.core.mail import send_mail
import json
from django.conf import settings
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from qsstats import QuerySetStats
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.db.models import Sum
from docxtpl import DocxTemplate
from django.http import JsonResponse

import csv

import os
from django.views.decorators.csrf import csrf_exempt,csrf_protect

@csrf_exempt
def statistics(request):
    startdate = datetime.strptime(request.POST['startdate'], '%d.%m.%Y')
    enddate = datetime.strptime(request.POST['enddate'], '%d.%m.%Y')
    paymentparking = paidparking.objects.filter(expirationdate__range=(startdate, enddate)).values('expirationdate').annotate(
        Sum('price'))
    paymentparking = paymentparking.order_by('expirationdate')
    return JsonResponse({'result': list(paymentparking)})
@csrf_exempt
def print_func(request):

    post_data = json.loads(request.body)
    date = post_data.get('date', False)
    price = post_data.get('price', False)
    pricesum = post_data.get('pricesum', False)

    #СSV файл
    FILENAME = "Статистика по продажам.csv"
    with open(FILENAME, "w", newline="") as file:
        columns = ["Date","Price"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        i = 0
        a = 0
        while i<len(date):
            while a < len(price):
                users = [
                    {"Date": date[i],"Price": price[a]},
                ]
                writer.writerows(users)
                i+=1
                a+=1
    #docx файл
    doc = DocxTemplate('template.docx')

    dates = date
    prices = price

    # Формируем список вида
    # [{'expirationdate': '2021-04-30', 'price': 1500},
    #  {'expirationdate': '2021-05-02', 'price': 450}, ...]
    tbl_contents = [{'expirationdate': expirationdate, 'price': price}
                    for expirationdate, price in zip(dates, prices)]

    context = {
        'tbl_contents': tbl_contents,
        'finalprice': sum(prices)
    }

    doc.render(context)
    doc.save("Статистика по продажам.docx")


    return JsonResponse({'result': 'fsd'})
def view_func(request):
    return render(request, 'index/statistics.html')

class ParkingView(APIView):
    def get(self, request):
        parking = Parking.objects.all()
        return Response({"parking": parking})

def index(request):
    parking = Parking.objects.all()
    return render(request, 'index/index.html', {'parking': parking})

def exit(request):
    if "phonenumber" in request.session:
        del request.session['phonenumber']
    return render(request, 'index/exit.html')

def session(request):
    if request.method == 'GET':
        phonenumber = request.GET["phonenumber"]
    request.session['phonenumber'] = phonenumber
    return HttpResponse("yes")

def enter(request):
    if "phonenumber" in request.session:
        return redirect('personalaccount')
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

                expirationdate = formparking.cleaned_data['expirationdate']
                PATTERN_OUT = "%d.%m.%Y."
                expirationdate = (datetime.strftime(expirationdate, PATTERN_OUT))
                expirationdate = str(expirationdate)

                expirationtime = formparking.cleaned_data['expirationtime']
                expirationtime = str(expirationtime)

                enddateandtime = formparking.cleaned_data['enddateandtime']
                PATTERN_OUT = "%d.%m.%Y. %H:%M"
                enddateandtime = (datetime.strftime(enddateandtime, PATTERN_OUT))
                enddateandtime = str(enddateandtime)

                send_mail('Оплата парковки в системе оплаты парковок', "Вас приветствует система оплаты парковок. Вы оплатили парковку по адресу: " + adress + ". Срок действия начинается с " + expirationdate + " " + expirationtime + " и заканчивается " + enddateandtime,'p_i.d.bukanov@mpt.ru',[formparking.cleaned_data['email']])
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

                expirationdate = formtickets.cleaned_data['expirationdate']
                PATTERN_OUT = "%d.%m.%Y."
                expirationdate = (datetime.strftime(expirationdate, PATTERN_OUT))
                expirationdate = str(expirationdate)

                expirationtime = formtickets.cleaned_data['expirationtime']
                expirationtime = str(expirationtime)

                enddateandtime = formtickets.cleaned_data['enddateandtime']
                PATTERN_OUT = "%d.%m.%Y. %H:%M"
                enddateandtime = (datetime.strftime(enddateandtime, PATTERN_OUT))
                enddateandtime = str(enddateandtime)

                send_mail('Оплата парковки в системе оплаты парковок',
                          "Вас приветствует система оплаты парковок. Вы оплатилиу " + nametickets + ". Срок действия начинается с " + expirationdate+ " " + expirationtime + " и заканчивается " + enddateandtime,
                          'p_i.d.bukanov@mpt.ru', [formtickets.cleaned_data['email']])
            formtickets.save()
            return redirect('home')
    else:
        formtickets = paidseasonticketsForm()
    return render(request, 'index/paymenttickets.html', {'formtickets': formtickets})

def personalaccount(request):
    if 'id' not in request.GET:
        pass
    else:
        id = request.GET["id"]
        try:
            user = users.objects.get(user_id=id)
            phonenumber = user.phonenumber
            request.session['phonenumber'] = phonenumber
        except users.DoesNotExist:
            return render(request, 'index/telegram.html')
    if "phonenumber" in request.session:
        if request.GET:
            if 'number' not in request.GET:
                phonenumber = request.session['phonenumber']
                phonenumber = str(phonenumber)
                paymentparking = paidparking.objects.filter(telephone=phonenumber)
                paymenttickets = paidseasontickets.objects.filter(telephone=phonenumber)
            else:
                phonenumber = "+"+request.GET["number"]
                phonenumber = phonenumber.replace(' ','')
                paymentparking = paidparking.objects.filter(telephone=phonenumber)
                paymenttickets = paidseasontickets.objects.filter(telephone=phonenumber)
                return render(request, 'index/personalaccount.html',
                              {'paymentparking': paymentparking, 'paymenttickets': paymenttickets})
        else:
            phonenumber = request.session['phonenumber']
            phonenumber = str(phonenumber)
            paymentparking = paidparking.objects.filter(telephone=phonenumber)
            paymenttickets = paidseasontickets.objects.filter(telephone=phonenumber)
    else:
        return render(request, 'index/enter.html')
    return render(request, 'index/personalaccount.html',{'paymentparking': paymentparking, 'paymenttickets': paymenttickets})

#Бот
def botparking(request):
    parking = list(Parking.objects.values())
    return JsonResponse(parking, safe=False)

def save_phonenumber(request):
    info='yes'
    if 'phonenumber' not in request.GET:
        pass
    else:
        phonenumber = request.GET["phonenumber"]
        phonenumber = f'+{phonenumber}'
        phonenumber = phonenumber.replace(' ', '')
    if 'user_id' not in request.GET:
        pass
    else:
        user_id = request.GET["user_id"]
    try:
        user = users.objects.get(user_id=user_id)
    except users.DoesNotExist:
        telegram = users
        telegram(user_id=user_id, phonenumber=phonenumber).save()
    return JsonResponse(info, safe=False)




