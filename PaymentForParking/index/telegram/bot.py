from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from telebot import types
from bs4 import BeautifulSoup
import requests

from config import TOKEN
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

import os
import sys
import django


sys.path.insert(0, os.path.abspath('../../'))
os.environ["DJANGO_SETTINGS_MODULE"] = "PaymentForParking.settings"
django.setup()
from index.models import users

button1 = KeyboardButton('Информация о парковках')
button2 = KeyboardButton('Тарифы на парковки')
button3 = KeyboardButton('Тарифы на абонементы')
button4 = KeyboardButton('Подтверждение номера телефона для авторизации на сайте')
button5 = KeyboardButton('Оплата парковки')
button6 = KeyboardButton('Оплата абонемента')

markup = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3).add(button4).add(button5).add(button6)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


#Обработка команды start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Вас приветствует система парковочных пространств.\nВыберите нужную функцию на клавиатуре", reply_markup=markup)

#Обработка события по нажатию на кнопку 'Подтверждение номера телефона для авторизации на сайте'
@dp.message_handler(lambda message: message.text == "Подтверждение номера телефона для авторизации на сайте")
async def process_hi6_command(message: types.Message):
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Отправить свой контакт ☎️', request_contact=True))
    await message.reply("Отправить свой номер телефона\nЭти две кнопки не зависят друг от друга", reply_markup=markup_request)

#Функция для определения id пользователя и номера телефона после отправки номера телефона
@dp.message_handler(content_types=['contact'])
async def contact(message: types.Message):
    if message.contact is not None:
        keyboard2 = ReplyKeyboardRemove()
        await message.reply("Вы успешно отправили свой номер",
                            reply_markup=keyboard2)
        global phonenumber
        phonenumber = str(message.contact.phone_number)
        user_id = str(message.contact.user_id)
        saving_to_the_database(phonenumber,user_id)

def saving_to_the_database(phonenumbe,user_id):
    try:
         user = users.objects.get(user_id=user_id)
    except users.DoesNotExist:
        print("error")
        telegram = users
        telegram(user_id=user_id, phonenumber=phonenumber).save()


#Обработка события по нажатию на кнопку 'Информация о парковках'
@dp.message_handler(lambda message: message.text == "Информация о парковках")
async def info_parking(message: types.Message):
    url = 'http://localhost/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    adress = soup.find_all('div', class_='adress')
    time = soup.find_all('div', class_='time')
    numberofseats = soup.find_all('div', class_='numberofavailableseats')
    for i in range(0, len(adress)):
        await message.reply(f'{adress[i].text}{time[i].text}{numberofseats[i].text}')
#Обработка события по нажатию на кнопку 'Тарифы на парковки'
@dp.message_handler(lambda message: message.text == "Тарифы на парковки")
async def pricingplans_parking(message: types.Message):
    url = 'http://localhost/pricingplans'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    adress = soup.find_all('div', class_='adress')
    mintime = soup.find_all('div', class_='mintime')
    price = soup.find_all('div', class_='price')
    bot.send_message(message.from_user.id, 'Тарифы на парковки:')
    for i in range(0, len(adress)):
        await message.reply(f'{adress[i].text}\n{mintime[i].text}\n{price[i].text}')

#Обработка события по нажатию на кнопку 'Тарифы на абонементы'
@dp.message_handler(lambda message: message.text == "Тарифы на абонементы")
async def pricingplans_parking(message: types.Message):
    url = 'http://localhost/pricingplans'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    adresstickets = soup.find_all('div', class_='adresstickets')
    numberofdays = soup.find_all('div', class_='numberofdays')
    validityperiod = soup.find_all('div', class_='validityperiod')
    pricetickets = soup.find_all('div', class_='pricetickets')
    bot.send_message(message.from_user.id, 'Тарифы на абонементы:')
    for i in range(0, len(numberofdays)):
        await message.reply(f'{adresstickets[i].text}\n{numberofdays[i].text}\n{validityperiod[i].text}\n{pricetickets[i].text}')

if __name__ == '__main__':
    executor.start_polling(dp)