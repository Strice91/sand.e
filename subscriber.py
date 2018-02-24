import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("Message: ", str(message.payload.decode("utf-8")))

def on_connect(client, userdata, flags, rc):
    print("Connected with result: " + str(rc))
    client.subscribe("sand.e.test")

print("Start Subscriber")

client_name="nsibfudqnwoezvfnoqwfez33240921"

client = mqtt.Client(client_name)
client.on_connect = on_connect
client.on_message = on_message
client.connect("mi5.itq.de", port=1883)

client.loop_forever()