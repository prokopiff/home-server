printenv > /etc/environment

python boot.py >> /logs/boot.log &
#python clock.py >> /logs/clock.log &

cron

tail -f /logs/*.log /var/log/cron.log
