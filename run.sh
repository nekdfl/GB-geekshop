#!/bin/bash

source ./venv/bin/activate

python3 ./geekshop/manage.py runserver 0.0.0.0:8000
