#!/bin/sh
python3 -m pip install -r tasks/requirements.txt
python3 tasks/manage.py migrate
echo '@reboot cd /home/ubuntu/tasks && ./run.sh' | crontab
export DJANGO_SUPERUSER_PASSWORD=cloud
export DJANGO_SUPERUSER_USERNAME=cloud
export DJANGO_SUPERUSER_EMAIL=cloud@a.com
python3 tasks/manage.py createsuperuser --noinput
