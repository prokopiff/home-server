import subprocess
import os
from influx_client import influx

keys = ["Server ID", "Sponsor", "Server Name", "Timestamp", "Distance", "Ping", "Download", "Upload", "Share", "IP Address"]

result = subprocess.Popen('/usr/local/bin/speedtest-cli --csv-delimiter "|" --csv',
			  shell = True, stdout = subprocess.PIPE).stdout.read().decode('utf-8')

print("Raw result:")
print(result)

values = result.split("|")

d = dict(zip(keys, values))

influx.write_point("internet_speed", {
            "download": float(d["Download"]),
            "upload": float(d["Upload"]),
            "ping": float(d["Ping"])
        })
