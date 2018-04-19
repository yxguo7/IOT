from guizero import App, Box, Text, TextBox, PushButton, Slider
from grovepi import *
import datetime
import time
import math
import grovepi
import sqlite3
import random

sensor = 3 
dbconnect = sqlite3.connect("./ac03.db")
pinMode(sensor, "INPUT")

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
   textTemp.value = temperature
   textHum.value = humidity
   add_readings(temperature, humidity)

 except KeyboardInterrupt:
  print("Exiting...")

 except IOError as IOe:
  print("An error has occured. %" % IOe)

 except Exception as e:
  print(e)

def exitProgram():
    app.destroy()

app = App(title="TCSS573: IoT Activity 03", height=300, width=500)
main = Text(app, text="Sensor Readings", size=14, font="Times New Roman", color="navy")
box = Box(app, layout="grid", grid=[1, 0])

textT = Text(box, text="Temperature", align="left", grid=[0, 0])
textH = Text(box, text="Humimity", align="left", grid=[0, 8])

textTemp = Text(box, text = "initializing", align="left", grid=[6, 0])
textHum = Text(box, text = "initializing", align="left", grid=[6, 8])
textTemp.repeat(1000, read_sensor)

exitButton = PushButton(box, command=exitProgram, text="Exit", grid=[2, 18])
exitButton.text_size = 16
app.display()























