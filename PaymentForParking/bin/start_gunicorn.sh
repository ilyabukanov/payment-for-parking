#!/bin/bash
source /mnt/c/WEB/codepython/PaymentForParking/env/bin/activate
exec gunicorn  -c "/mnt/c/WEB/codepython/PaymentForParking/PaymentForParking/gunicorn_config.py" PaymentForParking.wsgi

