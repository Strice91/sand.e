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
    pubSC.send(message.payload)

adress = "mi5.itq.de"
port = 1883

pubSC = SerialCon('/dev/ttyACM0')

sub1 = Subscriber()
pub = Publisher(adress, port)
sub1.mqttSubscribe(adress, port, on_message, "sand.e/motor/v")
pubSC.send("Start")

while True:
    pass

print("Turn Off")
