from subscriber import Subscriber
from publisher import Publisher
from keyController import KeyConroller
import time
import threading

def on_message(client, userdata, message):
    print(str(message.payload))

def refresh():
    pubKeyboard.mqttPublish("sand.e/motor/V", kc.v)
    pubKeyboard.mqttPublish("sand.e/motor/W", kc.w)
    threading.Timer(1, refresh, ()).start()

adress = "mi5.itq.de"
port = 1883

pubKeyboard = Publisher(adress, port)
kc = KeyConroller()

drive = threading.Thread(target=kc.drive)
drive.start()
refresh()

while True:
    pass