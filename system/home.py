import smbus
from influx_client import influx

# Get I2C bus
bus = smbus.SMBus(1)

# SHT31 address, 0x44(68)
# Send measurement command, 0x2C(44)
bus.write_i2c_block_data(0x44, 0x2C, [0x06])

# SHT31 address, 0x44(68)
# Read data back from 0x00(00), 6 bytes
# Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
data = bus.read_i2c_block_data(0x44, 0x00, 6)

# Convert the data
temp = data[0] * 256 + data[1]
cTemp = -45 + (175 * temp / 65535.0)
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

influx.write_point("home", {
            "temp": float(cTemp),
            "humidity": float(humidity)
        })
