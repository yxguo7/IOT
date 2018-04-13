from guizero import App, Box, Text, TextBox, PushButton, Slider
from grovepi import *
import time

myLED1 = 5 # blue
myLED2 = 6 # green
myLED3 = 7 # red

pinMode(myLED1, "OUTPUT")
pinMode(myLED2, "OUTPUT")
pinMode(myLED3, "OUTPUT")

def exitProgram():
    digitalWrite(myLED1, 0)
    app.destroy()

def sliderToggleLED1(slider_value):
    analogWrite(