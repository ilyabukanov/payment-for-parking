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

sys.path.insert(0, os.path.abspath('../../'))
os.environ["DJANGO_SETTINGS_MODULE"] = "PaymentForParking.settings"
django.setup()
from index.models import users,Parking



bot = telebot.TeleBot('1592020859:AAGxdEdp4NXigZXkXN90lz151ffHePpB_XQ')

keyboard = InlineKeyboardMarkup()
keyboard.row_width = 1
item_info = types.InlineKeyboardButton(text='Информация о парковках', callback_data='info')
item_parkingprice = types.InlineKeyboardButton(text='Тарифы на парковки', callback_data='pricingplansparking')
item_seasonticketprice  = types.InlineKeyboardButton(text='Тарифы на абонементы', callback_data='seasonticketprice')
item_phonenumber  = types.InlineKeyboardButton(text='Подтвердить номер телефона', callback_data='phonenumber')
item_payforparking  = types.InlineKeyboardButton(text='Оплатить парковку', callback_data='payforparking')
keyboard.add(item_info,item_parkingprice,item_seasonticketprice,item_phonenumber,item_payforparking)

#Функция получения номера телефона после подтверждения
@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Вы успешно отправили свой номер', reply_markup=keyboard2)
        global phonenumber
        phonenumber= str(message.contact.phone_number)
        user_id = str(message.contact.user_id)
        #try:
         #   user = users.objects.get(user_id=user_id)
       # except users.DoesNotExist:
         #   telegram = users
         #   telegram(user_id=user_id, phonenumber=phonenumber).save()
        response = requests.get(f'http://localhost/save_phonenumber?phonenumber={phonenumber}&user_id={user_id}')


@bot.message_handler(content_types='text')
def start_message(message):
    response = requests.get('http://localhost/botparking')
    global data
    data = response.json()
    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Вас приветствует система парковочных пространств.\nДоступные команды:\n',reply_markup = keyboard)

#Обработчик нажатия кнопок с адресами
@bot.callback_query_handler(lambda query: query.data.startswith("address_"))
def ans(query):
    chat_id = query.message.chat.id
    str = query.data
    res_str = str.replace('address_', '')
    print(res_str)
    address = query.data.split("_")[0] # адрес, с которым можно работать
    print(address)
#Функцию нажатия inline кнопок
@bot.callback_query_handler(func=lambda c:True)
def ans(c):
    cid = c.message.chat.id
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
    #Тарифы на парковки
    elif c.data == "pricingplansparking":
        bot.send_message(cid, 'Тарифы на парковки:')
        for d in data:
            adress = d['adress']
            minimaltimeforpayment = d['minimaltimeforpayment']
            price = d['price']
            text = f"Адрес: {adress}\nМинимальное время для оплаты: {minimaltimeforpayment}\nЦена: {price}"
            bot.send_message(cid, text)
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
    #Оплата парковок
    elif c.data == "payforparking":
        url = 'http://localhost/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        adress = soup.find_all('div', class_='adress')
        keyboard = InlineKeyboardMarkup()
        keyboard.row_width = 2
        for i in range(0, len(adress)):
            keyboard.add(InlineKeyboardButton(adress[i].text, callback_data=f"address_{adress[i].text}"))
        bot.send_message(cid, 'Выберите адрес парковки', reply_markup=keyboard)
    elif "ул." in c.data:
        print(c.data)



    elif c.data == "phonenumber":
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить телефон",
                                            request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(cid, 'Номер телефона',
                         reply_markup=keyboard)



if __name__ == '__main__':
    bot.polling(none_stop=True)
