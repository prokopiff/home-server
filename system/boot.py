from time import sleep
from influx_client import influx

sleep(10)

def post():
    influx.write_point("os", {'boot': 1})

for i in range(5):
    try:
        post()
        break
    except:
        sleep(30)
