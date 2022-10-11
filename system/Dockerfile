FROM python:3.10

RUN apt update && apt install -y cron rsyslog
RUN pip install RPi.GPIO psutil smbus pillow numpy influxdb_client speedtest-cli
RUN mkdir -p /logs/
RUN touch /logs/speedtest.log && touch /logs/system.log

WORKDIR /code
COPY *.py ./
COPY *.sh ./
COPY lib ./lib

COPY crontab /etc/cron.d/monitoring
RUN chmod 0644 /etc/cron.d/monitoring
RUN crontab /etc/cron.d/monitoring
RUN touch /var/log/cron.log

CMD sh run.sh
