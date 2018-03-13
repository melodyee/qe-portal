Start Redis:  (second instance on this machine)

sudo /usr/bin/redis-server /etc/redis/redis-qe-port.conf

Setup Flow to monitor Celery Tasks:

Enter /home/qe-ops/qe-dev/QE-PORTAL/qe_portal

celery -A qe_portal flower --port=5555