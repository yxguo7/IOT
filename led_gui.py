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
    digitalWrite(myLED2, 0)
    digitalWrite(myLED3, 0)
    app.destroy()

def sliderToggleLED1(slider_value):
    analogWrite(myLED1, int(slider_value))

def sliderToggleLED2(slider_value):
    analogWrite(myLED2, int(slider_value))

def sliderToggleLED3(slider_value):
    analogWrite(myLED3, int(slider_value))

def ledToggle1():
    button_status = digitalRead(myLED1)
    if (button_status == 0):
        digitalWrite(myLED1, 1)
        ledButton1.text = "Turn OFF"
        ledButton1.bg = "green"
        ledButton1.text_color = "white"
        textLED1.text_color = "green"
    else:
        digitalWrite(myLED1, 0)
        ledButton1.text = "Turn ON"
        ledButton1.bg = "red"
        textLED1.color = "black"

def ledToggle2():
    button_status = digitalRead(myLED2)
    if (button_status == 0):
        digitalWrite(myLED2, 1)
        ledButton2.text = "Turn OFF"
        ledButton2.bg = "green"
        ledButton2.text_color = "white"
        textLED2.text_color = "green"
    else:
        digitalWrite(myLED2, 0)
        ledButton2.text = "Turn ON"
        ledButton2.bg = "red"
        textLED2.color = "black"

def ledToggle3():
    button_status = digitalRead(myLED3)
    if (button_status == 0):
        digitalWrite(myLED3, 1)
        ledButton3.text = "Turn OFF"
        ledButton3.bg = "green"
        ledButton3.text_color = "white"
        textLED3.text_color = "green"
    else:
        digitalWrite(myLED3, 0)
        ledButton3.text = "Turn ON"
        ledButton3.bg = "red"
        textLED3.color = "black"

app = App(title="TCSS573: IoT Activity 02", height=300, width=500)
main = Text(app, text="LED Fading", size=14, font="Times New Roman", color="navy")
box = Box(app, layout="grid", grid=[1, 0])

textLED1 = Text(box, text="BLUE", align="left", grid=[0, 0])
ledButton1 = PushButton(box, command=ledToggle1, text="Turn ON", grid=[1, 0])
sliderLED1 = Slider(box, start=0, end=255, command=sliderToggleLED1, grid=[4, 0])

textLED2 = Text(box, text="GREEN", align="left", grid=[0, 8])
ledButton2 = PushButton(box, command=ledToggle2, text="Turn ON", grid=[1, 8])
sliderLED2 = Slider(box, start=0, end=255, command=sliderToggleLED2, grid=[4, 8])

textLED3 = Text(box, text="RED", align="left", grid=[0, 12])
ledButton3 = PushButton(box, command=ledToggle3, text="Turn ON", grid=[1, 12])
sliderLED3 = Slider(box, start=0, end=255, command=sliderToggleLED3, grid=[4, 12])



exitButton = PushButton(box, command=exitProgram, text="Exit", grid=[2, 18])
app.display()

