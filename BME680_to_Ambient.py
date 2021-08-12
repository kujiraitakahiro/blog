#!/usr/bin/env python

import bme680

try:
   sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
except IOError:
   sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

temperature = sensor.data.temperature
pressure = sensor.data.pressure
humidity = sensor.data.humidity

import ambient

ambi = ambient.Ambient(xxxxx, "xxxxxxxxxxxxxxxx") # Ambient's channel & writekey

r = ambi.send({"d1": pressure, "d2": temperature, "d3": humidity})
