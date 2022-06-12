import psutil
import os
from time import sleep
from datetime import datetime
from sys import argv
from influx_client import influx

psutil.PROCFS_PATH = "/host-proc"

if len(argv) > 1:
    sleep(int(argv[1]))

la = psutil.getloadavg()

mem = psutil.virtual_memory()

disk = psutil.disk_usage("/")

temp = psutil.sensors_temperatures()

boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S %Z")

users = len(psutil.users())

processes = len(psutil.pids())

influx.write_point("cpu", {
            "loadavg1": float(la[0]),
            "loadavg5": float(la[1]),
            "loadavg15": float(la[2])
        })

influx.write_point("mem", {
	        "pct_used": float(mem.percent)
        })

influx.write_point("disk", {
            "pct_used": float(disk.percent)
        })

influx.write_point("temp", {
            "cpu_temp_c": float(temp['cpu_thermal'][0].current)
        })

influx.write_point("os", {
            "last_boot_time": boot_time,
	        "users": users,
            "processes": processes
        })
