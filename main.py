from subscriber import Subscriber
from publisher import Publisher
from keyController import KeyConroller
from serialCon import SerialCon
import time
import threading

vPrev = 0
wPrev = 0
t = 0

def on_message(client, userdata, message):
    print(str(message.payload))

def refresh(controller):
    if controller.io:
        global t
        global vPrev
        global wPrev
        t += 1
        if (vPrev != kc.v) or (t >= 200):
            pubKeyboard.mqttPublish("sand.e/motor/v", kc.v)
            pubSC.send(kc.v)
            vPrev = kc.v
            t = 0
        if (wPrev != kc.w):
            pubKeyboard.mqttPublish("sand.e/motor/w", kc.w)
            wPrev = kc.w
            t =0
        threading.Timer(0.001, refresh, args=(controller,)).start()

adress = "mi5.itq.de"
port = 1883

pubSC = SerialCon('/dev/ttyAMA0')

pubKeyboard = Publisher(adress, port)
kc = KeyConroller()

drive = threading.Thread(target=kc.drive)
drive.start()
refresh(kc)

while kc.io:
    pass

print("Turn Off")
