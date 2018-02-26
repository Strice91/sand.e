from subscriber import Subscriber
from publisher import Publisher
from serialCon import SerialCon
import time
import threading

vPrev = ""
wPrev = ""
t = 0
subData = ""

def on_message(client, userdata, message):
    print(message.payload)
    subData = message.payload

def refresh():
    global t
    global vPrev
    global wPrev
    t += 1
    if (vPrev != subData) or (t >= 200):
        pubSC.send(subData)
        vPrev = subData
        t = 0

    threading.Timer(0.001, refresh, args=()).start()

adress = "mi5.itq.de"
port = 1883

pubSC = SerialCon('/dev/ttyACM0')

sub1 = Subscriber()
sub2 = Subscriber()
pub = Publisher(adress, port)
sub1.mqttSubscribe(adress, port, on_message, "sand.e/motor/v")
sub2.mqttSubscribe(adress, port, on_message, "sand.e/motor/w")
refresh(kc)

while True:
    pass

print("Turn Off")
