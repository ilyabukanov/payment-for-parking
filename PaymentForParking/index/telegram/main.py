import telebot #это pytelegrambotapi
from bs4 import BeautifulSoup
from telebot import types
import requests
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import os
import sys
import django
import ast
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

sys.path.insert(0, os.path.abspath('../../'))
os.environ["DJANGO_SETTINGS_MODULE"] = "PaymentForParking.settings"
django.setup()
from index.models import users,Parking

global chat_id



bot = telebot.TeleBot('1592020859:AAGxdEdp4NXigZXkXN90lz151ffHePpB_XQ')

keyboard = InlineKeyboardMarkup()
keyboard.row_width = 1
item_info = types.InlineKeyboardButton(text='Информация о парковках', callback_data='info')
item_parkingprice = types.InlineKeyboardButton(text='Тарифы на парковки', callback_data='pricingplansparking')
item_seasonticketprice  = types.InlineKeyboardButton(text='Тарифы на абонементы', callback_data='seasonticketprice')
item_phonenumber  = types.InlineKeyboardButton(text='Подтвердить номер телефона', callback_data='phonenumber')
item_payforparking  = types.InlineKeyboardButton(text='Оплатить парковку', callback_data='payforparking')
item_payfortickets  = types.InlineKeyboardButton(text='Оплатить абонемент на парковки', callback_data='payfortickets')
keyboard.add(item_info,item_parkingprice,item_seasonticketprice,item_phonenumber,item_payforparking, item_payfortickets)
global cid


def expiration_time(message):
    global expirationtime
    expirationtime = message.text
    bot.delete_message(chat_id, timestart.id)
#Функция для каллендаря парковок
@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=1))
def cal(c):
    result, key, step = DetailedTelegramCalendar(calendar_id=1).process(c.data)
    if not result and key:
        bot.edit_message_text(f"Выберите  {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.delete_message(c.message.chat.id, c.message.message_id)
        #bot.edit_message_text(c.message.chat.id, c.message.message_id)
        global date
        date = f'{result}'
        global timestart
        timestart = bot.send_message(c.message.chat.id,
                                'Выберите время начала срока действия')
        bot.register_next_step_handler(timestart, expiration_time)
#Функция для каллендаря с абонементами
@bot.callback_query_handler(func=DetailedTelegramCalendar.func(calendar_id=2))
def cal(c):
    result, key, step = DetailedTelegramCalendar(calendar_id=2).process(c.data)
    if not result and key:
        bot.edit_message_text(f"Выберите  {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.delete_message(c.message.chat.id, c.message.message_id)
        #bot.edit_message_text(c.message.chat.id, c.message.message_id)
        global date
        date = f'{result}'
        global timestart
        timestart = bot.send_message(c.message.chat.id,
                                'Выберите время начала срока действия')
        bot.register_next_step_handler(timestart, expiration_time)

#Функция получения номера телефона после подтверждения
@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Вы успешно отправили свой номер', reply_markup=keyboard2)
        bot.send_message(cid, 'Доступные команды:\n', reply_markup=keyboard)
        global phonenumber
        phonenumber= str(message.contact.phone_number)
        user_id = str(message.contact.user_id)
        response = requests.get(f'http://localhost/save_phonenumber?phonenumber={phonenumber}&user_id={user_id}')

#Обработки команды start
@bot.message_handler(content_types='text')
def start_message(message):
    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Вас приветствует система парковочных пространств.\nДоступные команды:\n',reply_markup = keyboard)

#Обработка введённых данных при указании времени для оплаты
def minimal_time_for_payment(message):
    global minimaltimeforpayment
    minimaltimeforpayment = message.text
    bot.delete_message(chat_id, time.id)
    calendar, step = DetailedTelegramCalendar(calendar_id=1).build()
    bot.send_message(message.chat.id,
                         f"Выберите {LSTEP[step]}",
                         reply_markup=calendar)
#Обработка введённых данных пользователя при указании номера автомобиля при оплате парковки
def car_number(message):
    global carnumber
    carnumber = message.text
    bot.delete_message(chat_id, number.id)
    response = requests.get(f'http://localhost/minimum_time_for_payment?adress={res_str}')
    data = response.json()
    minimaltimeforpayment = data['minimaltimeforpayment']
    global price
    price = data['price']
    global time
    time = bot.send_message(message.chat.id, f'Укажите время для оплаты.\nМинимальное время {minimaltimeforpayment}.')
    bot.register_next_step_handler(time, minimal_time_for_payment)

#Обработка введённых данных пользователя при указании номера автомобиля при оплате абонемента
def car_number_tickets(message):
    global carnumber_tickets
    carnumber_tickets = message.text
    bot.delete_message(message.chat.id, number_tickets.id)
    calendar, step = DetailedTelegramCalendar(calendar_id=2,locale='en').build()
    bot.send_message(message.chat.id,
                         f"Выберите {LSTEP[step]}",
                         reply_markup=calendar)


#Обработчик нажатия кнопок с адресами
@bot.callback_query_handler(lambda query: query.data.startswith("address_"))
def ans(query):
    global chat_id
    chat_id = query.message.chat.id
    str = query.data
    global res_str
    res_str = str.replace('address_', '')
    bot.delete_message(cid, res.id)
    global number
    number = bot.send_message(cid, 'Введите номер автомобиля.')
    bot.register_next_step_handler(number, car_number)


#Обработчик нажатия кнопок с наименованием абонемента
@bot.callback_query_handler(lambda query: query.data.startswith("res_str"))
def ans(query):
    global chat_id_tickets
    chat_id_tickets = query.message.chat.id
    str = query.data
    global res_str
    res_str = str.replace('res_str', '')
    bot.delete_message(cid, tickets.id)
    global number_tickets
    number_tickets = bot.send_message(cid, 'Введите номер автомобиля.')
    bot.register_next_step_handler(number_tickets, car_number_tickets)




#Функцию нажатия inline кнопок
@bot.callback_query_handler(func=lambda c:True)
def ans(c):
    global cid


    cid = c.message.chat.id
    response = requests.get('http://localhost/botparking')
    global data
    data = response.json()
    #Информация о парковках
    if c.data == "info":
        bot.send_message(cid, 'Информация о парковках:')
        for d in data:
            adress = d['adress']
            starttime = d['starttime']
            endtime = d['endtime']
            numberofavailableseats = d['numberofavailableseats']
            text = f"Адрес: {adress}\nВремя работы: {starttime} - {endtime}\nКоличество свободных мест: {numberofavailableseats}"
            bot.send_message(cid, text)

        bot.send_message(cid, 'Доступные команды:\n', reply_markup=keyboard)
    #Тарифы на парковки
    elif c.data == "pricingplansparking":
        bot.send_message(cid, 'Тарифы на парковки:')
        for d in data:
            adress = d['adress']
            minimaltimeforpayment = d['minimaltimeforpayment']
            price = d['price']
            text = f"Адрес: {adress}\nМинимальное время для оплаты: {minimaltimeforpayment}\nЦена: {price}"
            bot.send_message(cid, text)
        bot.send_message(cid, 'Доступные команды:\n', reply_markup=keyboard)

    #Тарифы на абонементы
    elif c.data == "seasonticketprice":
        url = 'http://localhost/pricingplans'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        adresstickets = soup.find_all('div', class_='adresstickets')
        numberofdays = soup.find_all('div', class_='numberofdays')
        validityperiod = soup.find_all('div', class_='validityperiod')
        pricetickets = soup.find_all('div', class_='pricetickets')
        bot.send_message(cid, 'Тарифы на абонементы:')
        for i in range(0, len(numberofdays)):
            bot.send_message(cid,
                             f'{adresstickets[i].text}\n{numberofdays[i].text}\n{validityperiod[i].text}\n{pricetickets[i].text}')
        bot.send_message(cid, 'Доступные команды:\n', reply_markup=keyboard)
    #Оплата парковок
    elif c.data == "payforparking":
        response = requests.get('http://localhost/adress_parking')
        data = response.json()
        keyboard_parking = InlineKeyboardMarkup()
        keyboard_parking.row_width = 2
        for d in data:
            adress = d['adress']
            keyboard_parking.add(InlineKeyboardButton(adress, callback_data=f"address_{adress}"))
        cid = c.message.chat.id
        bot.send_message(cid, 'Оплата парковки:')
        global res
        res = bot.send_message(cid, 'Выберите адрес парковки', reply_markup=keyboard_parking)


    # Оплата абонементов
    elif c.data == "payfortickets":
        response = requests.get('http://localhost/season_tickets')
        data_tickets = response.json()
        keyboard_tickets = InlineKeyboardMarkup()
        for d in data_tickets:
            nameseasontickets = d['nameseasontickets']
            res_str = nameseasontickets.replace('Абонемент для парковки', '')
            keyboard_tickets.add(InlineKeyboardButton(res_str, callback_data=f"res_str_{res_str}"))
        bot.send_message(c.message.chat.id, 'Оплата абонемента:')
        global tickets
        tickets = bot.send_message(cid, 'Выберите наименование абонемента', reply_markup=keyboard_tickets)


    #Подтверждение номера телефона
    elif c.data == "phonenumber":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить телефон",
                                            request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(cid, 'Номер телефона', reply_markup=keyboard)



if __name__ == '__main__':
    bot.polling(none_stop=True)
