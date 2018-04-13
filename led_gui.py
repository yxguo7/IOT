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

def sliderToggleLED(led, slider_value):
    analogWrite(led, int(slider_value))

def ledToggle(led, button, text):
    myLED = led
    ledButton = button
    textLED = text
    button_status = digitalRead(myLED)
    if (button_status == 0):
        digitalWrite(myLED, 1)
        ledButton.text = "Turn OFF"
        ledButton.bg = "green"
        ledButton.text_color = "white"
        textLED.text_color = "green"
    else:
        digitalWrite(myLED, 0)
        ledButton.text = "Turn ON"
        ledButton.bg = "red"
        textLED.color = "black"

app = App(title="TCSS573: IoT Activity 02", height=300, width=500)
main = Text(app, text="LED Fading", size=14, font="Times New Roman", color="navy")
box = Box(app, layout="grid", grid=[1, 0])

textLED1 = Text(box, text="BLUE", align="left", grid=[0, 0])
ledButton1 = PushButton(box, command=ledToggle(myLED1, ledButton1, textLED1), text="Turn ON", grid=[1, 0])
sliderLED1 = Slider(box, start=0, end=255, command=sliderToggleLED(myLED1), grid=[4, 0])

textLED2 = Text(box, text="GREEN", align="left", grid=[0, 0])
ledButton2 = PushButton(box, command=ledToggle(myLED2, ledButton2, textLED2), text="Turn ON", grid=[1, 0])
sliderLED2 = Slider(box, start=0, end=255, command=sliderToggleLED(myLED2), grid=[4, 0])

textLED3 = Text(box, text="RED", align="left", grid=[0, 0])
ledButton3 = PushButton(box, command=ledToggle(myLED3, ledButton3, textLED3), text="Turn ON", grid=[1, 0])
sliderLED3 = Slider(box, start=0, end=255, command=sliderToggleLED(myLED3), grid=[4, 0])



exitButton = PushButton(box, command=exitProgram, text="Exit", grid=[2, 8])
app.display()

