import time
import datetime
import math
import grovepi
import sqlite3
import random
import urllib2
from grovepi import *
from grove_rgb_lcd import *

""" Initial """
myLED = 2
pinMode(myLED, "OUTPUT")

sensor = 3
dbconnect = sqlite3.connect("./pp.db")

key = "GY3WHLQWR3WSYU3F"

""" send data to ThingSpeak"""
def sendThingSpeak(temp, hum):
 baseURL = "http://api.thingspeak.com/update?api_key=%s&field1=%s&field2=%s" % (key, temp, hum)
 print(baseURL)
 f = urllib2.urlopen(baseURL)
 print (f.read())
 f.close()
 print("sending data to ThinkSpeak....")


""" Temperature and Humidity sensor """
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
   print("Temp = %.2f Cel\tHumid = %.2f% %" % (temperature, humidity))
   add_readings(temperature, humidity)
   
   """ show on LCD """
   setText("Temp = %.2f CelHumid = %.2f% %" % (temperature, humidity))
   setRGB(0,128,64)

   sendThingSpeak(temperature, humidity)   

 except KeyboardInterrupt:
  print("Exiting...")

 except IOError as IOe:
  print("An error has occured. %" % IOe)

 except Exception as e:
  print(e)

""" LED """
def LED(on):
 try:
  if on==1:
   digitalWrite(myLED, 1)
   print("LED ON")
  else:
   digitalWrite(myLED, 0)
   print("LED OFF")

 except KeyboardInterrupt:
  digitalWrite(myLED, 0)

 except IOError:
  print("Error")


""" RUN """

digitalWrite(myLED, 0)
setText("")
setRGB(0,128,64)

while True:
 try:
  LED(1)
  read_sensor()
  time.sleep(3.00)
  LED(0)
  time.sleep(12.00)

 except KeyboardInterrupt:
   LED(0)
   setText("")
   setRGB(255, 255, 255)

 except IOError:
  print("Error")

digitalWrite(myLED, 0)
dbconnect.close()
