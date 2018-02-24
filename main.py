from subscriber import Subscriber
from publisher import Publisher
import time

def on_message(client, userdata, message):
    print(str(message.payload))

adress = "mi5.itq.de"
port = 1883

sub1 = Subscriber()
sub1.mqttSubscribe(adress, port, on_message, "sand.e")

while true:
    time.wait(2)