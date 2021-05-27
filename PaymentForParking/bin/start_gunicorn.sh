#!/bin/bash
source /home/ibukanov/code/payment-for-parking/PaymentForParking/env/bin/activate
exec gunicorn  -c "/home/ibukanov/code/payment-for-parking/PaymentForParking/PaymentForParking/gunicorn_config.py" PaymentForParking.wsgi

