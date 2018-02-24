from subscriber import Subscriber
from publisher import Publisher
from keyController import KeyConroller
import time
import _thread

def on_message(client, userdata, message):
    print(str(message.payload))

adress = "mi5.itq.de"
port = 1883

#sub1 = Subscriber()
#sub1.mqttSubscribe(adress, port, on_message, "sand.e")

pubKeyboard = Publisher(adress, port)
kc = KeyConroller()

_thread.start_new_thread(kc.drive, ())

while True:
    pubKeyboard.mqttPublish("sand.e/motor/V", kc.v)
    pubKeyboard.mqttPublish("sand.e/motor/W", kc.w)
    time.sleep(1)