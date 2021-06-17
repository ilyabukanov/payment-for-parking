import telebot #это pytelegrambotapi
from bs4 import BeautifulSoup
from telebot import types
import requests
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import ast
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
import re
from datetime import datetime, timedelta
from datetime import datetime
from datetime import time

global chat_id

global numberofdays







bot = telebot.TeleBot('1592020859:AAGxdEdp4NXigZXkXN90lz151ffHePpB_XQ')

mm = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
button1 = types.KeyboardButton("Информация 🅿️")
button2 = types.KeyboardButton("Тарифы 💸")
button3 = types.KeyboardButton("Подтверждение 📞")
button4 = types.KeyboardButton("Оплата 💳")
mm.add(button1,button2, button3, button4)

global cid

#Часы при оплате парковок
global keyboardhour
keyboardhour = InlineKeyboardMarkup()
keyboardhour.row_width = 3
zero = types.InlineKeyboardButton(text='00', callback_data=f"hour_{'00'}")
one = types.InlineKeyboardButton(text='01', callback_data=f"hour_{'01'}")
two = types.InlineKeyboardButton(text='02', callback_data=f"hour_{'02'}")
three = types.InlineKeyboardButton(text='03',callback_data=f"hour_{'03'}")
four = types.InlineKeyboardButton(text='04',callback_data=f"hour_{'04'}")
five = types.InlineKeyboardButton(text='05',callback_data=f"hour_{'05'}")
six = types.InlineKeyboardButton(text='06',callback_data=f"hour_{'06'}")
seven = types.InlineKeyboardButton(text='07',callback_data=f"hour_{'07'}")
eight = types.InlineKeyboardButton(text='08',callback_data=f"hour_{'08'}")
nine = types.InlineKeyboardButton(text='09',callback_data=f"hour_{'09'}")
ten = types.InlineKeyboardButton(text='10',callback_data=f"hour_{'10'}")
eleven = types.InlineKeyboardButton(text='11',callback_data=f"hour_{'11'}")
twelve = types.InlineKeyboardButton(text='12',callback_data=f"hour_{'12'}")
thirteen = types.InlineKeyboardButton(text='13',callback_data=f"hour_{'13'}")
fourteen = types.InlineKeyboardButton(text='14',callback_data=f"hour_{'14'}")
fifteen = types.InlineKeyboardButton(text='15',callback_data=f"hour_{'15'}")
sixteen  = types.InlineKeyboardButton(text='16',callback_data=f"hour_{'16'}")
seventeen = types.InlineKeyboardButton(text='17',callback_data=f"hour_{'17'}")
eighteen = types.InlineKeyboardButton(text='18',callback_data=f"hour_{'18'}")
nineteen = types.InlineKeyboardButton(text='19',callback_data=f"hour_{'19'}")
twenty = types.InlineKeyboardButton(text='20',callback_data=f"hour_{'20'}")
twentyone = types.InlineKeyboardButton(text='21',callback_data=f"hour_{'21'}")
twentytwo = types.InlineKeyboardButton(text='22',callback_data=f"hour_{'22'}")
twentythree = types.InlineKeyboardButton(text='23',callback_data=f"hour_{'23'}")
keyboardhour.add(zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree)

#Часы при оплате абонементов
global keyboardhourtickets
keyboardhourtickets = InlineKeyboardMarkup()
keyboardhourtickets.row_width = 3
zero = types.InlineKeyboardButton(text='00', callback_data=f"ticketshour_{'00'}")
one = types.InlineKeyboardButton(text='01', callback_data=f"ticketshour_{'01'}")
two = types.InlineKeyboardButton(text='02',
                                    callback_data=f"ticketshour_{'02'}")
three = types.InlineKeyboardButton(text='03',callback_data=f"ticketshour_{'03'}")
four = types.InlineKeyboardButton(text='04',callback_data=f"ticketshour_{'04'}")
five = types.InlineKeyboardButton(text='05',callback_data=f"ticketshour_{'05'}")
six = types.InlineKeyboardButton(text='06',callback_data=f"ticketshour_{'06'}")
seven = types.InlineKeyboardButton(text='07',callback_data=f"ticketshour_{'07'}")
eight = types.InlineKeyboardButton(text='08',callback_data=f"ticketshour_{'08'}")
nine = types.InlineKeyboardButton(text='09',callback_data=f"ticketshour_{'09'}")
ten = types.InlineKeyboardButton(text='10',callback_data=f"ticketshour_{'10'}")
eleven = types.InlineKeyboardButton(text='11',callback_data=f"ticketshour_{'11'}")
twelve = types.InlineKeyboardButton(text='12',callback_data=f"ticketshour_{'12'}")
thirteen = types.InlineKeyboardButton(text='13',callback_data=f"ticketshour_{'13'}")
fourteen = types.InlineKeyboardButton(text='14',callback_data=f"ticketshour_{'14'}")
fifteen = types.InlineKeyboardButton(text='15',callback_data=f"ticketshour_{'15'}")
sixteen  = types.InlineKeyboardButton(text='16',callback_data=f"ticketshour_{'16'}")
seventeen = types.InlineKeyboardButton(text='17',callback_data=f"ticketshour_{'17'}")
eighteen = types.InlineKeyboardButton(text='18',callback_data=f"ticketshour_{'18'}")
nineteen = types.InlineKeyboardButton(text='19',callback_data=f"ticketshour_{'19'}")
twenty = types.InlineKeyboardButton(text='20',callback_data=f"ticketshour_{'20'}")
twentyone = types.InlineKeyboardButton(text='21',callback_data=f"ticketshour_{'21'}")
twentytwo = types.InlineKeyboardButton(text='22',callback_data=f"ticketshour_{'22'}")
twentythree = types.InlineKeyboardButton(text='23',callback_data=f"ticketshour_{'23'}")
keyboardhourtickets.add(zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree)



#Минуты при оплате парковок
global keyboardminutes
keyboardminutes = InlineKeyboardMarkup()
keyboardminutes.row_width = 3
zero = types.InlineKeyboardButton(text='00', callback_data=f"minutes_{'00'}")
one = types.InlineKeyboardButton(text='01', callback_data=f"minutes_{'01'}")
two = types.InlineKeyboardButton(text='02',
                                    callback_data=f"minutes_{'02'}")
three = types.InlineKeyboardButton(text='03',callback_data=f"minutes_{'03'}")
four = types.InlineKeyboardButton(text='04',callback_data=f"minutes_{'04'}")
five = types.InlineKeyboardButton(text='05',callback_data=f"minutes_{'05'}")
six = types.InlineKeyboardButton(text='06',callback_data=f"minutes_{'06'}")
seven = types.InlineKeyboardButton(text='07',callback_data=f"minutes_{'07'}")
eight = types.InlineKeyboardButton(text='08',callback_data=f"minutes_{'08'}")
nine = types.InlineKeyboardButton(text='09',callback_data=f"minutes_{'09'}")
ten = types.InlineKeyboardButton(text='10',callback_data=f"minutes_{'10'}")
eleven = types.InlineKeyboardButton(text='11',callback_data=f"minutes_{'11'}")
twelve = types.InlineKeyboardButton(text='12',callback_data=f"minutes_{'12'}")
thirteen = types.InlineKeyboardButton(text='13',callback_data=f"minutes_{'13'}")
fourteen = types.InlineKeyboardButton(text='14',callback_data=f"minutes_{'14'}")
fifteen = types.InlineKeyboardButton(text='15',callback_data=f"minutes_{'15'}")
sixteen  = types.InlineKeyboardButton(text='16',callback_data=f"minutes_{'16'}")
seventeen = types.InlineKeyboardButton(text='17',callback_data=f"minutes_{'17'}")
eighteen = types.InlineKeyboardButton(text='18',callback_data=f"minutes_{'18'}")
nineteen = types.InlineKeyboardButton(text='19',callback_data=f"minutes_{'19'}")
twenty = types.InlineKeyboardButton(text='20',callback_data=f"minutes_{'20'}")
twentyone = types.InlineKeyboardButton(text='21',callback_data=f"minutes_{'21'}")
twentytwo = types.InlineKeyboardButton(text='22',callback_data=f"minutes_{'22'}")
twentythree = types.InlineKeyboardButton(text='23',callback_data=f"minutes_{'23'}")
twentyfour = types.InlineKeyboardButton(text='24',callback_data=f"minutes_{'24'}")
twentyfive = types.InlineKeyboardButton(text='25',callback_data=f"minutes_{'25'}")
twentysix = types.InlineKeyboardButton(text='26',callback_data=f"minutes_{'26'}")
twentyseven = types.InlineKeyboardButton(text='27',callback_data=f"minutes_{'27'}")
twentyeight = types.InlineKeyboardButton(text='28',callback_data=f"minutes_{'28'}")
twentynine = types.InlineKeyboardButton(text='29',callback_data=f"minutes_{'29'}")
thirty = types.InlineKeyboardButton(text='30',callback_data=f"minutes_{'30'}")
thirtyone = types.InlineKeyboardButton(text='31',callback_data=f"minutes_{'31'}")
thirtytwo = types.InlineKeyboardButton(text='32',callback_data=f"minutes_{'32'}")
thirtythree = types.InlineKeyboardButton(text='33',callback_data=f"minutes_{'33'}")
thirtyfour = types.InlineKeyboardButton(text='34',callback_data=f"minutes_{'34'}")
thirtyfive = types.InlineKeyboardButton(text='35',callback_data=f"minutes_{'35'}")
thirtysix = types.InlineKeyboardButton(text='36',callback_data=f"minutes_{'36'}")
thirtyseven = types.InlineKeyboardButton(text='37',callback_data=f"minutes_{'37'}")
thirtyeight = types.InlineKeyboardButton(text='38',callback_data=f"minutes_{'38'}")
thirtynine = types.InlineKeyboardButton(text='39',callback_data=f"minutes_{'39'}")
forty = types.InlineKeyboardButton(text='40',callback_data=f"minutes_{'40'}")
fortyone = types.InlineKeyboardButton(text='41',callback_data=f"minutes_{'41'}")
fortytwo = types.InlineKeyboardButton(text='42',callback_data=f"minutes_{'42'}")
fortythree = types.InlineKeyboardButton(text='43',callback_data=f"minutes_{'43'}")
fortyfour  = types.InlineKeyboardButton(text='44',callback_data=f"minutes_{'44'}")
fortyfive = types.InlineKeyboardButton(text='46',callback_data=f"minutes_{'45'}")
fortysix = types.InlineKeyboardButton(text='46',callback_data=f"minutes_{'46'}")
fortyseven = types.InlineKeyboardButton(text='47',callback_data=f"minutes_{'47'}")
fortyeight = types.InlineKeyboardButton(text='48',callback_data=f"minutes_{'48'}")
fortynine = types.InlineKeyboardButton(text='49',callback_data=f"minutes_{'49'}")
fifty = types.InlineKeyboardButton(text='50',callback_data=f"hour_{'50'}")
fiftyone = types.InlineKeyboardButton(text='51',callback_data=f"minutes_{'51'}")
fiftytwo = types.InlineKeyboardButton(text='52',callback_data=f"minutes_{'52'}")
fiftythree = types.InlineKeyboardButton(text='53',callback_data=f"minutes_{'53'}")
fiftyfour = types.InlineKeyboardButton(text='54',callback_data=f"minutes_{'54'}")
fiftyfive = types.InlineKeyboardButton(text='55',callback_data=f"minutes_{'55'}")
fiftysix = types.InlineKeyboardButton(text='56',callback_data=f"minutes_{'56'}")
fiftyseven = types.InlineKeyboardButton(text='57',callback_data=f"minutes_{'57'}")
fiftyeight = types.InlineKeyboardButton(text='58',callback_data=f"minutes_{'58'}")
fiftynine = types.InlineKeyboardButton(text='59',callback_data=f"minutes_{'59'}")
keyboardminutes.add(zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty,thirtyone,thirtytwo,thirtythree,thirtyfour,thirtyfive,thirtysix,thirtyseven,thirtyeight,thirtynine,	forty,fortyone,fortytwo,fortythree,fortyfour,fortyfive,fortysix,fortyseven,	fortyeight,fortynine,fifty,	fiftyone,fiftytwo,fiftythree,fiftyfour,fiftyfive,fiftysix,fiftyseven,fiftyeight,fiftynine)


#Минуты при оплате абонементов
global keyboardminutestickets
keyboardminutestickets = InlineKeyboardMarkup()
keyboardminutestickets.row_width = 3
zero = types.InlineKeyboardButton(text='00', callback_data=f"ticketsminutes_{'00'}")
one = types.InlineKeyboardButton(text='01', callback_data=f"ticketsminutes_{'01'}")
two = types.InlineKeyboardButton(text='02',
                                    callback_data=f"ticketsminutes_{'02'}")
three = types.InlineKeyboardButton(text='03',callback_data=f"ticketsminutes_{'03'}")
four = types.InlineKeyboardButton(text='04',callback_data=f"ticketsminutes_{'04'}")
five = types.InlineKeyboardButton(text='05',callback_data=f"ticketsminutes_{'05'}")
six = types.InlineKeyboardButton(text='06',callback_data=f"ticketsminutes_{'06'}")
seven = types.InlineKeyboardButton(text='07',callback_data=f"ticketsminutes_{'07'}")
eight = types.InlineKeyboardButton(text='08',callback_data=f"ticketsminutes_{'08'}")
nine = types.InlineKeyboardButton(text='09',callback_data=f"ticketsminutes_{'09'}")
ten = types.InlineKeyboardButton(text='10',callback_data=f"ticketsminutes_{'10'}")
eleven = types.InlineKeyboardButton(text='11',callback_data=f"ticketsminutes_{'11'}")
twelve = types.InlineKeyboardButton(text='12',callback_data=f"ticketsminutes_{'12'}")
thirteen = types.InlineKeyboardButton(text='13',callback_data=f"ticketsminutes_{'13'}")
fourteen = types.InlineKeyboardButton(text='14',callback_data=f"ticketsminutes_{'14'}")
fifteen = types.InlineKeyboardButton(text='15',callback_data=f"ticketsminutes_{'15'}")
sixteen  = types.InlineKeyboardButton(text='16',callback_data=f"ticketsminutes_{'16'}")
seventeen = types.InlineKeyboardButton(text='17',callback_data=f"ticketsminutes_{'17'}")
eighteen = types.InlineKeyboardButton(text='18',callback_data=f"ticketsminutes_{'18'}")
nineteen = types.InlineKeyboardButton(text='19',callback_data=f"ticketsminutes_{'19'}")
twenty = types.InlineKeyboardButton(text='20',callback_data=f"ticketsminutes_{'20'}")
twentyone = types.InlineKeyboardButton(text='21',callback_data=f"ticketsminutes_{'21'}")
twentytwo = types.InlineKeyboardButton(text='22',callback_data=f"ticketsminutes_{'22'}")
twentythree = types.InlineKeyboardButton(text='23',callback_data=f"ticketsminutes_{'23'}")
twentyfour = types.InlineKeyboardButton(text='24',callback_data=f"ticketsminutes_{'24'}")
twentyfive = types.InlineKeyboardButton(text='25',callback_data=f"ticketsminutes_{'25'}")
twentysix = types.InlineKeyboardButton(text='26',callback_data=f"ticketsminutes_{'26'}")
twentyseven = types.InlineKeyboardButton(text='27',callback_data=f"ticketsminutes_{'27'}")
twentyeight = types.InlineKeyboardButton(text='28',callback_data=f"ticketsminutes_{'28'}")
twentynine = types.InlineKeyboardButton(text='29',callback_data=f"ticketsminutes_{'29'}")
thirty = types.InlineKeyboardButton(text='30',callback_data=f"ticketsminutes_{'30'}")
thirtyone = types.InlineKeyboardButton(text='31',callback_data=f"ticketsminutes_{'31'}")
thirtytwo = types.InlineKeyboardButton(text='32',callback_data=f"ticketsminutes_{'32'}")
thirtythree = types.InlineKeyboardButton(text='33',callback_data=f"ticketsminutes_{'33'}")
thirtyfour = types.InlineKeyboardButton(text='34',callback_data=f"ticketsminutes_{'34'}")
thirtyfive = types.InlineKeyboardButton(text='35',callback_data=f"ticketsminutes_{'35'}")
thirtysix = types.InlineKeyboardButton(text='36',callback_data=f"ticketsminutes_{'36'}")
thirtyseven = types.InlineKeyboardButton(text='37',callback_data=f"ticketsminutes_{'37'}")
thirtyeight = types.InlineKeyboardButton(text='38',callback_data=f"ticketsminutes_{'38'}")
thirtynine = types.InlineKeyboardButton(text='39',callback_data=f"ticketsminutes_{'39'}")
forty = types.InlineKeyboardButton(text='40',callback_data=f"ticketsminutes_{'40'}")
fortyone = types.InlineKeyboardButton(text='41',callback_data=f"ticketsminutes_{'41'}")
fortytwo = types.InlineKeyboardButton(text='42',callback_data=f"ticketsminutes_{'42'}")
fortythree = types.InlineKeyboardButton(text='43',callback_data=f"ticketsminutes_{'43'}")
fortyfour  = types.InlineKeyboardButton(text='44',callback_data=f"ticketsminutes_{'44'}")
fortyfive = types.InlineKeyboardButton(text='46',callback_data=f"ticketsminutes_{'45'}")
fortysix = types.InlineKeyboardButton(text='46',callback_data=f"ticketsminutes_{'46'}")
fortyseven = types.InlineKeyboardButton(text='47',callback_data=f"ticketsminutes_{'47'}")
fortyeight = types.InlineKeyboardButton(text='48',callback_data=f"ticketsminutes_{'48'}")
fortynine = types.InlineKeyboardButton(text='49',callback_data=f"ticketsminutes_{'49'}")
fifty = types.InlineKeyboardButton(text='50',callback_data=f"ticketsminutes_{'50'}")
fiftyone = types.InlineKeyboardButton(text='51',callback_data=f"ticketsminutes_{'51'}")
fiftytwo = types.InlineKeyboardButton(text='52',callback_data=f"ticketsminutes_{'52'}")
fiftythree = types.InlineKeyboardButton(text='53',callback_data=f"ticketsminutes_{'53'}")
fiftyfour = types.InlineKeyboardButton(text='54',callback_data=f"ticketsminutes_{'54'}")
fiftyfive = types.InlineKeyboardButton(text='55',callback_data=f"ticketsminutes_{'55'}")
fiftysix = types.InlineKeyboardButton(text='56',callback_data=f"ticketsminutes_{'56'}")
fiftyseven = types.InlineKeyboardButton(text='57',callback_data=f"ticketsminutes_{'57'}")
fiftyeight = types.InlineKeyboardButton(text='58',callback_data=f"ticketsminutes_{'58'}")
fiftynine = types.InlineKeyboardButton(text='59',callback_data=f"ticketsminutes_{'59'}")
keyboardminutestickets.add(zero,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twentyone,twentytwo,twentythree,twentyfour,twentyfive,twentysix,twentyseven,twentyeight,twentynine,thirty,thirtyone,thirtytwo,thirtythree,thirtyfour,thirtyfive,thirtysix,thirtyseven,thirtyeight,thirtynine,	forty,fortyone,fortytwo,fortythree,fortyfour,fortyfive,fortysix,fortyseven,	fortyeight,fortynine,fifty,	fiftyone,fiftytwo,fiftythree,fiftyfour,fiftyfive,fiftysix,fiftyseven,fiftyeight,fiftynine)

#Inline кнопки для оплаты и отменя при оплате парковок
global keyboard_payment_parking_final
keyboard_payment_parking_final = InlineKeyboardMarkup()
keyboard_payment_parking_final.row_width = 1
payment = types.InlineKeyboardButton(text='✅ Оплатить', callback_data='payment_parking_final')
сancel = types.InlineKeyboardButton(text='❌ Отменить',
                                    callback_data='сancel')
keyboard_payment_parking_final.add(payment, сancel)

#Inline кнопки для оплаты и отменя при оплате абонементов
global keyboard_payment_tickets_final
keyboard_payment_tickets_final = InlineKeyboardMarkup()
keyboard_payment_tickets_final.row_width = 1
payment = types.InlineKeyboardButton(text='✅ Оплатить', callback_data='payment_tickets_final')
сancel = types.InlineKeyboardButton(text='❌ Отменить',
                                    callback_data='сancel')
keyboard_payment_tickets_final.add(payment, сancel)

#Обработки нажатия на кнопки
@bot.message_handler(content_types=['text'])
def handler(message):
   if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Вас приветствует система парковочных пространств.', reply_markup=mm)
   elif message.text == "Информация 🅿️":
       bot.send_message(message.chat.id, 'Информация о парковках:')
       response = requests.get(f'http://localhost/botparking?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168')
       data = response.json()
       for d in data:
           adress = d['adress']
           starttime = d['starttime']
           endtime = d['endtime']
           numberofavailableseats = d['numberofavailableseats']
           text = f"Адрес: {adress}\nВремя работы: {starttime} - {endtime}\nКоличество свободных мест: {numberofavailableseats}"
           bot.send_message(message.chat.id, text)
   elif message.text == "Тарифы 💸":
       keyboard = InlineKeyboardMarkup()
       keyboard.row_width = 1
       item_parkingprice = types.InlineKeyboardButton(text='На парковки', callback_data='pricingplansparking')
       item_seasonticketprice = types.InlineKeyboardButton(text='На абонементы',
                                                           callback_data='seasonticketprice')
       keyboard.add(item_parkingprice,item_seasonticketprice)
       bot.send_message(message.chat.id, 'Тарифы:',
                        reply_markup=keyboard)
   # Подтверждение номера телефона
   elif message.text == "Подтверждение 📞":
       keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
       button_phone = types.KeyboardButton(text="Отправить телефон",
                                           request_contact=True)
       keyboard.add(button_phone)
       bot.send_message(message.chat.id, 'Номер телефона', reply_markup=keyboard)
   elif message.text == "Оплата 💳":
       global keyboardpayment
       keyboardpayment = InlineKeyboardMarkup()
       keyboardpayment.row_width = 1
       payment_parking = types.InlineKeyboardButton(text='Парковок', callback_data='payment_parking')
       payment_season_ticket = types.InlineKeyboardButton(text='Абонементов',
                                                           callback_data='payment_season_ticket')
       keyboardpayment.add(payment_parking,payment_season_ticket)
       bot.send_message(message.chat.id, 'Оплата:',
                        reply_markup=keyboardpayment)


#Вывод всех данных оплаты парковки
def phone_number(message):
    global parking_phone_number
    parking_phone_number = message.text
    if not re.match('^((\+7)+([0-9]){10})$', parking_phone_number):
        bot.send_message(message.chat.id, "Номер телефона введён не верно(формат +7)")
        bot.send_message(message.chat.id, 'Оплата:',
                         reply_markup=keyboardpayment)
    else:
        bot.delete_message(message.chat.id, phonenumber.id)
        global sum_price
        sum_price = price * int(minimaltimeforpayment)
        global time_parking
        time_parking = time_hour + ":" + time_minutes
        date_time = date_parking + " " + time_parking
        additional_hours = int(minimaltimeforpayment)
        old_date = datetime.strptime(date_time, '%d.%m.%Y %H:%M')
        new_date = old_date + timedelta(hours=additional_hours)
        PATTERN_IN = "%Y-%m-%d %H:%M:%S"
        PATTERN_OUT = "%d.%m.%Y %H:%M"
        date = datetime.strptime(str(new_date), PATTERN_IN)
        global new_date_payment_parking
        new_date_payment_parking = datetime.strftime(date, PATTERN_OUT)
        PATTERN_IN = "%d.%m.%Y %H:%M"
        PATTERN_OUT = "%H:%M"
        date1 = datetime.strptime(str(new_date_payment_parking ), PATTERN_IN)
        date2 = datetime.strftime(date1, PATTERN_OUT)
        if start_time < date2 < end_time:
            global payment_final
            payment_final = bot.send_message(cid,
                                             f'Оплата парковки\nАдрес: {res_str}\nНомер автомобиля: {carnumber}\nКоличество времени: {minimaltimeforpayment} Час(а)(ов)\nЦена: {sum_price} Рублей\nНомер телефона: {parking_phone_number}\nДата начала срока действия: {date_parking}\nВремя начала срока действия: {time_parking}\nДата и время окончания срока действия: {new_date_payment_parking}',
                                             reply_markup=keyboard_payment_parking_final)
        else:
            bot.send_message(cid, "Выбрано большое количество времени. Время окончания срока дейтсвия оплаты не совпадает с временем работы парковки.")
            bot.send_message(cid, 'Оплата:',
                             reply_markup=keyboardpayment)


#Вывод всех данных оплаты абонемента
def phone_number_tickets(message):
    global tickets_phone_number
    tickets_phone_number = message.text
    if not re.match('^((\+7)+([0-9]){10})$', tickets_phone_number):
        bot.send_message(message.chat.id, "Номер телефона введён не верно(формат +7)")
        bot.send_message(message.chat.id, 'Оплата:',
                         reply_markup=keyboardpayment)
    else:
        bot.delete_message(message.chat.id, phonenumber_tickets.id)
        global time_tickets
        time_tickets = time_hour_tickets + ":" + time_minutes_tickets
        date_time = date_tickets + " " + time_tickets
        response = requests.get(f'http://localhost/number_of_days_tickets?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168&name_tickets={res_str_tickets}')
        data = response.json()
        number_of_days = data['number_of_days']
        additional_days = int(number_of_days)
        old_date = datetime.strptime(date_time, '%d.%m.%Y %H:%M')
        new_date = old_date + timedelta(days=additional_days)
        PATTERN_IN = "%Y-%m-%d %H:%M:%S"
        PATTERN_OUT = "%d.%m.%Y %H:%M"
        date = datetime.strptime(str(new_date), PATTERN_IN)
        global new_date_tickets
        new_date_tickets = datetime.strftime(date, PATTERN_OUT)
        global payment_final
        payment_final = bot.send_message(message.chat.id,
                     f'Оплата абонемента\nНаименование: {res_str_tickets}\nНомер автомобиля: {carnumber_tickets}\nЦена: {price_tickets}\nНомер телефона: {tickets_phone_number}\nДата начала срока действия: {date_tickets}\nВремя начала срока действия: {time_tickets}\nДата и время окончания срока действия: {new_date_tickets}', reply_markup=keyboard_payment_tickets_final)


#Указание номер телефона при оплате парковок
def expiration_time_tickets(message):
    global expirationtime_tickets
    expirationtime_tickets = message.text
    bot.delete_message(message.chat.id, timestart.id)
    global phonenumber_tickets
    phonenumber_tickets = bot.send_message(message.chat.id, 'Введите номер телефона (в формате +7).')
    bot.register_next_step_handler(phonenumber_tickets, phone_number_tickets)

#Указание номер телефона при оплате абонементов
def expiration_time(message):
    global expirationtime
    expirationtime = message.text
    bot.delete_message(chat_id, timestart.id)
    global phonenumber
    phonenumber = bot.send_message(message.chat.id, 'Введите номер телефона (в формате +7).')
    bot.register_next_step_handler(phonenumber, phone_number)



#Функция получения номера телефона после подтверждения
@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Вы успешно отправили свой номер', reply_markup=mm)
        global phonenumber
        phonenumber= str(message.contact.phone_number)
        user_id = str(message.contact.user_id)
        response = requests.get(f'http://localhost/save_phonenumber?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168&'
                                f'phonenumber={phonenumber}&user_id={user_id}')

#Функция для каллендаря парковок
@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def cal_parking(c):
    result, key, step = DetailedTelegramCalendar(calendar_id=1).process(c.data)
    if not result and key:
        bot.edit_message_text(f"Выберите дату начала срока действия",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.delete_message(c.message.chat.id, c.message.message_id)
        #bot.edit_message_text(c.message.chat.id, c.message.message_id)
        global date_parking
        date_parking = f'{result}'
        PATTERN_IN = "%Y-%m-%d"
        PATTERN_OUT = "%d.%m.%Y"
        date = datetime.strptime(str(date_parking), PATTERN_IN)
        date_parking = datetime.strftime(date, PATTERN_OUT)
        global hours
        hours = bot.send_message(c.message.chat.id,
                                'Выберите час начала срока действия',reply_markup=keyboardhour)
        #bot.register_next_step_handler(timestart, expiration_time)
#Функция для каллендаря с абонементами
@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def cal_titckets(c):
    result, key, step = DetailedTelegramCalendar(calendar_id=2).process(c.data)
    if not result and key:
        bot.edit_message_text(f"Выберите дату начала срока действия",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.delete_message(c.message.chat.id, c.message.message_id)
        #bot.edit_message_text(c.message.chat.id, c.message.message_id)
        global date_tickets
        date_tickets = f'{result}'
        PATTERN_IN = "%Y-%m-%d"
        PATTERN_OUT = "%d.%m.%Y"
        date = datetime.strptime(str(date_tickets), PATTERN_IN)
        date_tickets = datetime.strftime(date, PATTERN_OUT)
        global hours
        hours = bot.send_message(c.message.chat.id,
                                'Выберите час начала срока действия',reply_markup=keyboardhourtickets)
        #bot.register_next_step_handler(timestart, expiration_time)
#Обработка введённых данных при указании времени для оплаты
def minimal_time_for_payment(message):
    global minimaltimeforpayment
    minimaltimeforpayment = message.text
    minimaltimeforpayment = ''.join(re.findall('\d', minimaltimeforpayment))
    bot.delete_message(chat_id, time.id)
    print(minimaltime)
    print(minimaltimeforpayment)
    if minimaltimeforpayment<minimaltime:
        bot.send_message(message.chat.id, "Минимальное время для оплаты указано не верно. Оно меньше минимального времени, которое указано в тарифах.")
        bot.send_message(message.chat.id, 'Оплата:',
                         reply_markup=keyboardpayment)
    else:
        calendar, step = DetailedTelegramCalendar(calendar_id=1).build()
        bot.send_message(message.chat.id, "Выберите дату", reply_markup=calendar)


#Обработка введённых данных пользователя при указании номера автомобиля при оплате парковки
def car_number(message):
    global carnumber
    carnumber = message.text
    r = re.compile('[А-Я]\d{3}[А-Я]{2}\d{2,3}')
    if r.search(carnumber):
        bot.delete_message(chat_id, number.id)
        response = requests.get(f'http://localhost/minimum_time_for_payment?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168&adress={res_str}')
        data = response.json()
        minimaltimeforpayment = data['minimaltimeforpayment']
        global minimaltime
        minimaltime = data['minimaltimeforpayment']
        minimaltime = ''.join(re.findall('\d', minimaltime))
        global price
        price = data['price']
        global time
        time = bot.send_message(message.chat.id,
                                f'Укажите время для оплаты.\nМинимальное время {minimaltimeforpayment}.')
        bot.register_next_step_handler(time, minimal_time_for_payment)
    else:
        bot.send_message(message.chat.id, "Номер автомобиля введён не верно (формат: А000АА777 или АА000AA77)")
        bot.send_message(message.chat.id, 'Оплата:',
                         reply_markup=keyboardpayment)

#Обработчик нажатия кнопок с минутами при оплате абонементов
@bot.callback_query_handler(lambda query: query.data.startswith("ticketsminutes_"))
def tickets_minutes(query):
    str = query.data
    global time_minutes_tickets
    time_minutes_tickets = str.replace('ticketsminutes_', '')
    bot.delete_message(cid, minutes.id)
    global phonenumber_tickets
    phonenumber_tickets = bot.send_message(cid, 'Введите номер телефона (в формате +7).')
    bot.register_next_step_handler(phonenumber_tickets, phone_number_tickets)

#Обработчик нажатия кнопок с часами при оплате абонементов
@bot.callback_query_handler(lambda query: query.data.startswith("ticketshour_"))
def tickets_hour(query):
    str = query.data
    global time_hour_tickets
    time_hour_tickets = str.replace('ticketshour_', '')
    bot.delete_message(cid, hours.id)
    global minutes
    minutes = bot.send_message(cid,
                             'Выберите минуту начала срока действия', reply_markup=keyboardminutestickets)

#Обработчик нажатия кнопок с минутами при оплате парковок
@bot.callback_query_handler(lambda query: query.data.startswith("minutes_"))
def minutes_parking(query):
    str = query.data
    global time_minutes
    time_minutes = str.replace('minutes_', '')
    bot.delete_message(cid, minutes.id)
    time_parking = time_hour + ":" + time_minutes
    response = requests.get(
        f'http://localhost/start_time_end_time?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168&adress={res_str}')
    data = response.json()
    global start_time
    start_time = data['start_time']
    global end_time
    end_time = data['end_time']
    if start_time < time_parking < end_time:
        global phonenumber
        phonenumber = bot.send_message(cid, 'Введите номер телефона (в формате +7).')
        bot.register_next_step_handler(phonenumber, phone_number)
    else:
        bot.send_message(cid, "Время выбрано не верно. Парковка не работает.")
        bot.send_message(cid, 'Оплата:',
                         reply_markup=keyboardpayment)



#Обработчик нажатия кнопок с часами при оплате парковок
@bot.callback_query_handler(lambda query: query.data.startswith("hour_"))
def hour_parking(query):
    str = query.data
    global time_hour
    time_hour = str.replace('hour_', '')
    bot.delete_message(cid, hours.id)
    global minutes
    minutes = bot.send_message(cid,
                             'Выберите минуту начала срока действия', reply_markup=keyboardminutes)




#Обработчик нажатия кнопок с адресами
@bot.callback_query_handler(lambda query: query.data.startswith("address_"))
def adress_parking(query):
    global chat_id
    chat_id = query.message.chat.id
    str = query.data
    global res_str
    res_str = str.replace('address_', '')
    bot.delete_message(cid, res.id)
    global number
    number = bot.send_message(cid, 'Введите номер автомобиля.')
    bot.register_next_step_handler(number, car_number)

#Обработчик нажатия кнопки удалить при оплате
@bot.callback_query_handler(lambda query: query.data.startswith("сancel"))
def cancel_parking(query):
    bot.delete_message(cid, payment_final.id)
    bot.send_message(cid,"Вы успешно отменили оплату")

#Обработка введённых данных пользователя при указании номера автомобиля при оплате абонемента
def car_number_tickets(message):
    global carnumber_tickets
    carnumber_tickets = message.text
    r = re.compile('[А-Я]\d{3}[А-Я]{2}\d{2,3}')
    if r.search(carnumber_tickets):
        bot.delete_message(message.chat.id, number_tickets.id)
        response = requests.get(f'http://localhost/price_tickets?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168&name_tickets={res_str_tickets}')
        data = response.json()
        global price_tickets
        price_tickets = data['price']
        calendar, step = DetailedTelegramCalendar(calendar_id=2, locale='en').build()
       #bot.send_message(message.chat.id,
                        # f"Выберите {LSTEP[step]}",
                        # reply_markup=calendar)
        bot.send_message(message.chat.id,"Выберите дату начала срока действия", reply_markup=calendar)
    else:
        bot.send_message(message.chat.id, "Номер автомобиля введён не верно (формат: А000АА777 или АА000AA77)")
        bot.send_message(message.chat.id, 'Оплата:',
                         reply_markup=keyboardpayment)

#Обработчик нажатия кнопок с наименованием абонемента
@bot.callback_query_handler(lambda query: query.data.startswith("res_str"))
def name_tickets(query):
    global chat_id_tickets
    chat_id_tickets = query.message.chat.id
    str = query.data
    global res_str_tickets
    res_str_tickets = str.replace('res_str_', '')
    bot.delete_message(cid, tickets.id)
    global number_tickets
    number_tickets = bot.send_message(cid, 'Введите номер автомобиля.')
    bot.register_next_step_handler(number_tickets, car_number_tickets)

#Обработчик нажатия кнопки оплаты при оплате парковок
@bot.callback_query_handler(lambda query: query.data.startswith("payment_parking_final"))
def payment_parking(query):
    response = requests.get(
        f'http://localhost/save_payment_parking?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168&adress={res_str}&car_number={carnumber}&amount_of_time={minimaltimeforpayment}&price={sum_price}&telephone={parking_phone_number}&date_time_paid_parking={date_parking}&expiration_time={time_parking}&end_date_and_time={new_date_payment_parking}')

#Обработчик нажатия кнопки оплаты при оплате абонементов
@bot.callback_query_handler(lambda query: query.data.startswith("payment_tickets_final"))
def payment_tickets(query):
    response = requests.get(f'http://localhost/save_payment_tickets?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168&nametickets={res_str_tickets}&car_number_tickets={carnumber_tickets}&price_tickets={price_tickets}&telephone={tickets_phone_number}&date_tickets={date_tickets}&time_tickets={time_tickets}&new_date_tickets={new_date_tickets}')


#Функцию нажатия inline кнопок
@bot.callback_query_handler(func=lambda c:True)
def ans(c):
    global cid
    cid = c.message.chat.id
    #Тарифы на парковки
    if c.data == "pricingplansparking":
        bot.send_message(cid, 'Тарифы на парковки:')
        response = requests.get(f'http://localhost/botparking?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168')
        data = response.json()
        for d in data:
            adress = d['adress']
            minimaltimeforpayment = d['minimaltimeforpayment']
            price = d['price']
            text = f"Адрес: {adress}\nМинимальное время для оплаты: {minimaltimeforpayment}\nЦена: {price}"
            bot.send_message(cid, text)
    # Тарифы на абонементы
    elif c.data == "seasonticketprice":
        bot.send_message(cid, 'Тарифы на абонементы:')
        response = requests.get(f'http://localhost/season_tickets?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168')
        data = response.json()
        for d in data:
            nameseasontickets = d['nameseasontickets']
            numberofdays = d['numberofdays']
            time = d['time']
            price = d['price']
            text = f"Наиманование: {nameseasontickets}\nКоличество дней: {numberofdays}\nВремя работы: {time}\nЦена: {price} Рублей"
            bot.send_message(cid, text)

    # Оплата парковок
    elif c.data == "payment_parking":
        response = requests.get('http://localhost/adress_parking?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168')
        data = response.json()
        keyboard_parking = InlineKeyboardMarkup()
        keyboard_parking.row_width = 2
        for d in data:
            adress = d['adress']
            keyboard_parking.add(InlineKeyboardButton(adress, callback_data=f"address_{adress}"))
        cid = c.message.chat.id
        global res
        res = bot.send_message(cid, 'Выберите адрес парковки', reply_markup=keyboard_parking)

    # Оплата абонементов
    elif c.data == "payment_season_ticket":
        response = requests.get('http://localhost/season_tickets?token=162575CVE-17T2-9D1Z-5NT4-791Z58E14168')
        data_tickets = response.json()
        keyboard_tickets = InlineKeyboardMarkup()
        global price_tickets
        for d in data_tickets:
            nameseasontickets = d['nameseasontickets']
            price_tickets = d['price']
            res_str = nameseasontickets.replace('Абонемент для парковки', '')
            keyboard_tickets.add(InlineKeyboardButton(res_str, callback_data=f"res_str_{res_str}"))
        global tickets
        tickets = bot.send_message(cid, 'Выберите наименование абонемента', reply_markup=keyboard_tickets)


if __name__ == '__main__':
    bot.polling(none_stop=True)
