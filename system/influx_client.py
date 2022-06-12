from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import os
from datetime import datetime

__all__ = ["influx"]

class __Influx(object):
    def __init__(self) -> None:
        self.url = os.environ["INFLUX_URL"]
        self.token = os.environ["INFLUX_TOKEN"]
        self.org = os.environ["INFLUX_ORG"]
        self.bucket = os.environ["INFLUX_BUCKET"]
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write_point(self, measurement, fields, tags = {}) -> None:
        d = {
                'measurement': measurement,
                'tags': tags,
                'fields': fields,
                'time': datetime.utcnow()
            }
        print("Writing point: " + str(d))
        self.write_api.write(self.bucket, self.org, 
            Point.from_dict(d)
        )

influx = __Influx()
