import paho.mqtt.client as mqtt
import random

class Subscriber:
    def __init__(self):
        self.channel = None
        self.client = mqtt.Client(str(random.randint(0xf, 0xffff)))

    def on_con(self, client, userdata, flags, rc):
        print("Connected with result: " + str(rc))
        self.client.subscribe(self.channel)

    def mqttSubscribe(self, adress, port, onMSG, ch):
        print("Start subscription")
        self.channel = ch
        self.client.on_connect = self.on_con
        self.client.on_message = onMSG
        self.client.connect(adress, port)
        self.client.loop_forever()

    def mqttUnsubscribe(self):
        self.client.loop_stop()
        self.client.unsubscribe()
        self.client.disconnect()