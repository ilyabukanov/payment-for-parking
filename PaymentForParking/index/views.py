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
from django.core.files import File
from io import BytesIO
from django.core.mail import EmailMessage

import csv

import os
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this

#Статистика по продажам
@csrf_exempt
def statistics(request):
    startdate = datetime.strptime(request.POST['startdate'], '%d.%m.%Y')
    enddate = datetime.strptime(request.POST['enddate'], '%d.%m.%Y')
    paymentparking = paidparking.objects.filter(expirationdate__range=(startdate, enddate)).values('expirationdate').annotate(
        Sum('price'))
    paymentparking = paymentparking.order_by('expirationdate')
    return JsonResponse({'result': list(paymentparking)})

#Отображение шаблона видеозображения
def video_images_from_cameras(request):
    parking = Parking.objects.all()
    return render(request,'index/video_images_from_cameras.html',{"parking": parking})

#Получени ссылки на видеоизображение
def video(request):
    adress = request.GET["adress"]
    parking = Parking.objects.get(adress=adress)
    return JsonResponse({'video': parking.videofromthecamera})

#Формирование отчётных документов по продажам в формате WORD
@csrf_exempt
def print_func(request):

    post_data = json.loads(request.body)
    date = post_data.get('date', False)
    price = post_data.get('price', False)
    pricesum = post_data.get('pricesum', False)
    startdate = post_data.get('startdate', False)
    enddate = post_data.get('enddate', False)
    email_adres = post_data.get('email', False)


    #docx файл
    doc = DocxTemplate('template.docx')
    dates = date
    prices = price
    tbl_contents = [{'expirationdate': expirationdate, 'price': price}
                    for expirationdate, price in zip(dates, prices)]
    PATTERN_IN = "%Y-%m-%d"
    PATTERN_OUT = "%d.%m.%Y"
    date_start = datetime.strptime(str(startdate), PATTERN_IN)
    new_date_start = datetime.strftime(date_start, PATTERN_OUT)
    date_end = datetime.strptime(str(enddate), PATTERN_IN)
    new_date_end = datetime.strftime(date_end, PATTERN_OUT)
    context = {
        'tbl_contents': tbl_contents,
        'finalprice': sum(prices),
        'startdate': new_date_start,
        'enddate': new_date_end
    }
    doc.render(context)
    file_io = BytesIO()
    doc.save(file_io)
    email = EmailMessage(subject="Отчётный документ по продажам", body=f"Отчётный документ по продажам с "
    f"{new_date_start} по {new_date_end}", from_email="p_i.d.bukanov@mpt.ru",
                         to=[email_adres])
    email.attach("Статистика по продажам.docx", file_io.getvalue(),
                 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    email.send()


    return JsonResponse({'result': 'fsd'})

#Отображение шаблона со статистикой
@csrf_exempt
def view_func(request):
    return render(request, 'index/statistics.html')

#Получение объектов парковки
class ParkingView(APIView):
    def get(self, request):
        parking = Parking.objects.all()
        return Response({"parking": parking})

#Отображение шаблона главной со страницей
@csrf_exempt
def index(request):
    parking = Parking.objects.all()
    return render(request, 'index/index.html', {'parking': parking})

#Выход из личного кабинета
@csrf_exempt
def exit(request):
    if "phonenumber" in request.session:
        del request.session['phonenumber']
    return render(request, 'index/exit.html')

#Работа с сессией
@csrf_exempt
def session(request):
    if request.method == 'GET':
        phonenumber = request.GET["phonenumber"]
    request.session['phonenumber'] = phonenumber
    return HttpResponse("yes")

#Вход в личный кабинет
@csrf_exempt
def enter(request):
    if "phonenumber" in request.session:
        return redirect('personalaccount')
    return render(request, 'index/enter.html')

#Отображение шаблона с тарифами
@csrf_exempt
def pricingplans(request):
    parking = Parking.objects.all()
    return render(request, 'index/pricingplans.html',  {'parking': parking})

#Оплата парковки
@csrf_exempt
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

#Получение цены и минимального времени парковки
@csrf_exempt
def valuesubstitution(request):
    if request.method == 'GET':
        adress = request.GET["adress"]
        try:
            parking = Parking.objects.get(adress=adress)
            return JsonResponse({'price': parking.price, 'minimaltimeforpayment': parking.minimaltimeforpayment})
        except Parking.DoesNotExist:
            pass
    else:
        pass
    return HttpResponse("Записи с данным адресом не найдена")
@csrf_exempt

#Получение цены абонемента
def seasonticketprice(request):
    if request.method == 'GET':
        nametickets = request.GET["nametickets"]
        seasontickets = tickets.objects.get(nameseasontickets=nametickets)
        return JsonResponse({'price': seasontickets.price, 'numberofdays': seasontickets.numberofdays})
    else:
        pass

#Оплата абонементов
@csrf_exempt
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

#Личный кабинет
@csrf_exempt
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

global token
token = "162575CVE-17T2-9D1Z-5NT4-791Z58E14168"


#Функция, которая получает все данные о парковках и отправляет их в telegram bot
@csrf_exempt
def botparking(request):
    token_bot = request.GET["token"]
    if(token_bot == token):
        parking = list(Parking.objects.values())
        return JsonResponse(parking, safe=False)

#Функция сохранения номера телефона при подтверждении в telegram
@csrf_exempt
def save_phonenumber(request):

    info='yes'
    token_bot = request.GET["token"]
    if (token_bot == token):
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

#Получение минимального времени для оплаты по определённому адресу
@csrf_exempt
def minimum_time_for_payment(request):
    token_bot = request.GET["token"]
    if (token_bot == token):
        if 'adress' not in request.GET:
            pass
        else:
            adress = request.GET["adress"]
            parking = Parking.objects.get(adress=adress)
            return JsonResponse({'minimaltimeforpayment': parking.minimaltimeforpayment, 'price': parking.price})

#Получение всех данные о парковках для оплаты
@csrf_exempt
def adress_parking(request):
    token_bot = request.GET["token"]
    if (token_bot == token):
        parking = list(Parking.objects.values())
        return JsonResponse(parking, safe=False)

#Получение всех данных о абонементах для оплаты
@csrf_exempt
def season_tickets(request):
    token_bot = request.GET["token"]
    if (token_bot == token):
        seasontickets = list(tickets.objects.values())
        return JsonResponse(seasontickets, safe=False)

#Получение цены выбранного абонемента при оплате
@csrf_exempt
def price_tickets(request):
    token_bot = request.GET["token"]
    if (token_bot == token):
        if 'name_tickets' not in request.GET:
            pass
        else:
            name_tickets = request.GET["name_tickets"]
            ticketss = tickets.objects.get(nameseasontickets=name_tickets)
            return JsonResponse({'price': ticketss.price})

#Получение количество дней действия абонемента при оплате
@csrf_exempt
def number_of_days_tickets(request):
    token_bot = request.GET["token"]
    if (token_bot == token):
        if 'name_tickets' not in request.GET:
            pass
        else:
            name_tickets = request.GET["name_tickets"]
            ticketss = tickets.objects.get(nameseasontickets=name_tickets)
            return JsonResponse({'number_of_days': ticketss.numberofdays})

#Сохранение оплаченной парковки
@csrf_exempt
def save_payment_parking(request):
    token_bot = request.GET["token"]
    if (token_bot == token):
        adress = request.GET["adress"]
        carnumber = request.GET["car_number"]
        amountoftime = request.GET["amount_of_time"]
        price = request.GET["price"]
        telephone = request.GET["telephone"]
        expirationdate = request.GET["date_time_paid_parking"]
        expirationtime = request.GET["expiration_time"]
        enddateandtime = request.GET["end_date_and_time"]
        addr = Parking.objects.get(adress=adress)
        telephone = "+" + telephone
        telephone = telephone.replace(' ', '')
        PATTERN_IN = "%d.%m.%Y"
        PATTERN_OUT = "%Y-%m-%d"
        date_expirationdate = datetime.strptime(str(expirationdate), PATTERN_IN)
        new_expirationdate = datetime.strftime(date_expirationdate, PATTERN_OUT)
        PATTERN_IN_enddateandtime  = "%d.%m.%Y %H:%M"
        PATTERN_OUT_enddateandtime  = "%Y-%m-%d %H:%M:%S"
        date_expirationdate_enddateandtime = datetime.strptime(str(enddateandtime), PATTERN_IN_enddateandtime)
        new_expirationdate_enddateandtime = datetime.strftime(date_expirationdate_enddateandtime, PATTERN_OUT_enddateandtime)



    save_payment_parking = paidparking
    save_payment_parking(adress=addr,carnumber=carnumber,amountoftime=amountoftime,price=price,telephone=telephone,expirationdate=new_expirationdate,expirationtime=expirationtime,enddateandtime=new_expirationdate_enddateandtime).save()

#Сохранение оплаченного абонемента
@csrf_exempt
def save_payment_tickets(request):
    token_bot = request.GET["token"]
    if (token_bot == token):
        nametickets = request.GET["nametickets"]
        carnumber = request.GET["car_number_tickets"]
        price = request.GET["price_tickets"]
        telephone = request.GET["telephone"]
        expirationdate = request.GET["date_tickets"]
        expirationtime = request.GET["time_tickets"]
        enddateandtime = request.GET["new_date_tickets"]
        nameseasontickets = tickets.objects.get(nameseasontickets=nametickets)
        telephone = "+" + telephone
        telephone = telephone.replace(' ', '')
        PATTERN_IN = "%d.%m.%Y"
        PATTERN_OUT = "%Y-%m-%d"
        date_expirationdate = datetime.strptime(str(expirationdate), PATTERN_IN)
        new_expirationdate = datetime.strftime(date_expirationdate, PATTERN_OUT)
        PATTERN_IN_enddateandtime  = "%d.%m.%Y %H:%M"
        PATTERN_OUT_enddateandtime  = "%Y-%m-%d %H:%M:%S"
        date_expirationdate_enddateandtime = datetime.strptime(str(enddateandtime), PATTERN_IN_enddateandtime)
        new_expirationdate_enddateandtime = datetime.strftime(date_expirationdate_enddateandtime, PATTERN_OUT_enddateandtime)
        save_payment_tickets = paidseasontickets
        save_payment_tickets(nametickets=nameseasontickets,carnumber=carnumber,price=price, telephone=telephone, expirationdate=new_expirationdate,expirationtime=expirationtime,enddateandtime= new_expirationdate_enddateandtime).save()

#Получение времени начала и окончания работы парковки
@csrf_exempt
def start_time_end_time(request):
    token_bot = request.GET["token"]
    if (token_bot == token):
        adress = request.GET["adress"]
        parking = Parking.objects.get(adress=adress)
        return JsonResponse({'start_time': parking.starttime, 'end_time': parking.endtime})




















