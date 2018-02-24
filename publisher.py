import paho.mqtt.client as mqtt
import random

class Publisher:

    def __init__(self, addr, port):
        print("Start publisher")
        self.client = mqtt.Client(str(random.randint(0xf, 0xffff)))
        self.client.connect(addr, port)

    def mqttPublish(self, topic, msg):
        self.client.publish(topic, msg)