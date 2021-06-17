Данный файл содержит инструкцию по развёртке WEB-приложения на сервере
В данном примере использовалась WSL Debian 10
Для начала необходимо скачать Debian в Microsoft Store
В данном примере использовалось следующие дерево директории:
```
C:\WEB\codepython:
```
Фото: https://imgur.com/xjZwjzf

PaymentForParking – это само приложения 
```
C:\WEB\codepython\PaymentForParking
```
Фото: https://imgur.com/goUPw9Q
```
C:\WEB\codepython\PaymentForParking\
```
Фото: https://imgur.com/wm9dzR7
***
# Обновление репозиториев
***
```
sudo apt-get update && sudo apt-get -y upgrade
```
***
# Установка начального софта
***
```
sudo apt-get install -y vim mosh tmux htop git curl wget unzip zip gcc build-essential 
```
***
# Установка необходимого софта из репозиториев
***
```
sudo apt-get install -y zsh tree redis-server nginx zlib1g-dev libbz2-dev libreadline-dev llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev liblzma-dev python3-dev python-pil python3-lxml libxslt-dev python-libxml2 python-libxslt1 libffi-dev libssl-dev python-dev gnumeric libsqlite3-dev libpq-dev libxml2-dev libxslt1-dev libjpeg-dev libfreetype6-dev libcurl4-openssl-dev supervisor
```
***
# Установка последней версии python из исходников
***
```
wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz

sudo tar xvf Python-3.9.1.*	

cd Python-3.9.1	  	

sudo ./configure --enable-optimizations --prefix=/.python	(./configure --enable-optimizations --with-ensurepip=install)

sudo make -j 8 

sudo make altinstall
```
***
# Создание директории под проект
***
```
mkdir PaymentForParking
```
***
# Создание виртуального окружения:
***
```
sudo python3.9 -m venv env

source env/bin/activate
```
***
# Установка pip и Django
***
```
sudo apt-get install -y python3-pip
pip3 -V
sudo pip3 install Django
```
***
# Создание Django проекта:
***
```
django-admin startproject PaymentForParking
cd PaymentForParking

Запуск сервера для теста

sudo python3 manage.py runserver 0.0.0.0:8000
```
***
# Gunicorn
***
```
sudo pip3 install gunicorn
cd /mnt/c/WEB/codepython/PaymentForParking/PaymentForParking
vim gunicorn_config.py
command='/mnt/c/WEB/codepython/PaymentForParking/PaymentForParking/env/bin/gunicorn'
pythonpath='/mnt/c/WEB/codepython/PaymentForParking/PaymentForParkinPaymentForParking'
bind = '127.0.0.1:8001'
workers = 3
user = 'ilya'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=PaymentForParking.settings'
```
Фото: https://imgur.com/D77LNv3
```
cd /mnt/c/WEB/codepython/PaymentForParking
mkdir bin
cd bin
vim start_gunicorn.sh

	#!/bin/bash
	source /mnt/c/WEB/codepython/PaymentForParking/env/bin/activate
	exec gunicorn  -c " /mnt/c/WEB/codepython/PaymentForParking/PaymentForParking/gunicorn_config.py" PaymentForParking.wsgi
```
Фото: https://imgur.com/vKv000V
```
sudo chmod +x start_gunicorn.sh


. ./bin/start_gunicorn.sh – запуск gunicorn через bash скрипт 
```
***
# Настройка Nginx
***
```
sudo vim /etc/nginx/sites-enabled/

server {
listen 80 default_server;
listen [::]:80 default_server;


root /var/ilya/html;

index index.html index.html index.nginx-debian.html

server_name _;

location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
     root /mnt/c/WEB/codepython/PaymentForParking;
}

Location / {
                           proxy_pass http://127.0.0.1:8001;
                           proxy_set_header X-Forwarded-Host $server_name;
                           proxy_set_header X-Real_IP $remove_addr;
                           add_header P3P ‘CP=”ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV”’;
                           add_header Access-Control-Allow-Origin *;
                           }
}
```
Фото: https://imgur.com/dNLTigS
```
sudo nginx
```
***
# Статика
***

Идём в файл settings.py и вставляем в конец файла STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

Импортируем os – import os
```
python3 manage.py collectstatic
    
```
***
# PostgreSQL
***
```
sudo apt install postgresql postgresql-contrib
pip install psycopg2-binary
sudo service postgresql start
sudo -u postgres psql
CREATE DATABASE PaymentForParking;
CREATE USER paymentforparkinguser WITH PASSWORD 'R8Tn8jDn';
ALTER ROLE paymentforparkinguser SET client_encoding TO 'utf8';
ALTER ROLE paymentforparkinguser SET default_transaction_isolation TO 'read committed';
ALTER ROLE paymentforparkinguser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE paymentforparking TO paymentforparkinguser;
\q
```
Sudo nano settings.py:
Фото: https://imgur.com/m3vWCvM
```
python3 manage.py makemigrations
python3 manage.py migrate
```
***
# Работа с проектом
Для работы с проектом необходимо ознакомиться с приложением в "Руководство Пользователя"
Ссылка на сайт: "https://demo.vidim.org/"
Данные для входа в админ-панель находяться в файле "Данные.txt"
Все необходимые библиотеки для работы находяться в файле "requirements.txt"
Для установки всех библиотек из файле необходимо использовать следующую команду
```
pip3 install -r requirements.txt
```





