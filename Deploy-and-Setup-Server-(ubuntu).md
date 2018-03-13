Database Readonly:

chown www-data:www-data /srv/mysite   
chown www-data:www-data /srv/mysite/DATABASE.sqlite

_________

Broker:
https://www.rabbitmq.com/install-debian.html

Setup rabbitmq for Celery:

sudo apt-get update

sudo apt-get install erlang

sudo apt-get install rabbitmq-server

sudo apt-get install redis-server

Python support redis:
$ sudo pip install redis

Setup Broker for Celery:
http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html


_________

sync code:

1.copy to /var/www/qe-port/

2.copy deplop/qe_port_product to /qe-port/, override wsgi.py, celery.py, settings.py.

3.change permission for sqlite db. 

chown www-data:www-data /srv/mysite   
chown www-data:www-data /srv/mysite/DATABASE.sqlite

-------------------------
Setup Flower for celery task monitor

sudo pip install flower


-------------------------
### Server setup

1.Start RabbitMQ

sudo rabbitmq-server


2.Start Redis:  (second instance on this machine)

sudo /usr/bin/redis-server /etc/redis/redis-qe-port.conf

3.Setup Flow to monitor Celery Tasks:

Enter /home/qe-ops/qe-dev/QE-PORTAL/qe_portal

celery flower -A qe_portal --address=0.0.0.0 --port=5555

then brower: http://localhost:5555