printenv > /etc/environment

python boot.py >> /logs/boot.log &
#python clock.py >> /logs/clock.log &
python poe_hat.py >> /logs/poe_hat.log &

cron

tail -f /logs/*.log /var/log/cron.log
