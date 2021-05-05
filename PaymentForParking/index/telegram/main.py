import telebot #это pytelegrambotapi
import psycopg2 #для работы с базами данных
from bs4 import BeautifulSoup
from telebot import types
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
import requests
import json



import os
import sys
import django

sys.path.insert(0, os.path.abspath('../../'))
os.environ["DJANGO_SETTINGS_MODULE"] = "PaymentForParking.settings"
django.setup()
from index.models import users

bot = telebot.TeleBot('1592020859:AAGxdEdp4NXigZXkXN90lz151ffHePpB_XQ')
@bot.message_handler(commands=['phonenumber'])
def phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить телефон",
                                        request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Номер телефона',
                     reply_markup=keyboard)
@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Вы успешно отправили свой номер', reply_markup=keyboard2)
        global phonenumber
        phonenumber= str(message.contact.phone_number)
        user_id = str(message.contact.user_id)
        try:
            user = users.objects.get(user_id=user_id)
        except users.DoesNotExist:
            telegram = users
            telegram(user_id=user_id, phonenumber=phonenumber).save()



@bot.message_handler(content_types='text')
def start_message(message):
    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Вас приветствует система парковочных пространств.\nДоступные команды:\n/info - информация о парковках\n/parkingprice - тарифы на парковки\n/seasonticketprice - тарифы на абонементы\n/phonenumber - подтверждение телефонного номера')
        response = requests.post('https://ru.stackoverflow.com', json={"key": "value"})
        print(response.json())
    elif message.text.lower() == '/info':
        url = 'http://localhost/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        adress = soup.find_all('div', class_='adress')
        time = soup.find_all('div', class_='time')
        numberofseats = soup.find_all('div', class_='numberofavailableseats')
        bot.send_message(message.from_user.id, 'Наши парковки:')
        for i in range(0, len(adress)):
            bot.send_message(message.from_user.id, f'{adress[i].text}{time[i].text}{numberofseats[i].text}')
    elif message.text.lower() == '/parkingprice':
        url = 'http://localhost/pricingplans'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        adress = soup.find_all('div', class_='adress')
        mintime = soup.find_all('div', class_='mintime')
        price = soup.find_all('div', class_='price')
        bot.send_message(message.from_user.id, 'Тарифы на парковки:')
        for i in range(0, len(adress)):
            bot.send_message(message.from_user.id, f'{adress[i].text}\n{mintime[i].text}\n{price[i].text}')
    elif message.text.lower() == '/seasonticketprice':
        url = 'http://localhost/pricingplans'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        adresstickets = soup.find_all('div', class_='adresstickets')
        numberofdays = soup.find_all('div', class_='numberofdays')
        validityperiod = soup.find_all('div', class_='validityperiod')
        pricetickets = soup.find_all('div', class_='pricetickets')
        bot.send_message(message.from_user.id, 'Тарифы на абонементы:')
        for i in range(0, len(numberofdays)):
           bot.send_message(message.from_user.id,
                             f'{adresstickets[i].text}\n{numberofdays[i].text}\n{validityperiod[i].text}\n{pricetickets[i].text}')

if __name__ == '__main__':
    bot.polling(none_stop=True)
