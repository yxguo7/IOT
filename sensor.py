import datetime
import time
import math
import grovepi
import sqlite3
import random

sensor = 3
dbconnect = sqlite3.connect("./ac03.db")

def add_readings(temp, hum):
 cursor = dbconnect.cursor()
 ID = random.randrange(100000, 999999)
 cursor.execute("INSERT INTO sensorData values(?, ?, ?, datetime('now'))", (ID, temp, hum))
 dbconnect.commit()

def read_sensor():
 try:
  [temp, hum] = grovepi.dht(sensor, 0)
  if ((math.isnan(temp) == False) and (math.isnan(hum) == False) and (hum >=0)):
   temperature = temp
   humidity = hum
   print("Temperature = %.2f Celsius\tHumidity = %.2f% %" % (temperature, humidity))
   add_readings(temperature, humidity)

 except KeyboardInterrupt:
  print("Exiting...")

 except IOError as IOe:
  print("An error has occured. %" % IOe)

 except Exception as e:
  print(e)

while (1):
 read_sensor()
 time.sleep(1)

dbconnect.close()
