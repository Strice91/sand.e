import paho.mqtt.client as mqtt
import time

print("Start Publisher")

client_name="kjncsifgnfoiweuhf4334235"

client = mqtt.Client(client_name)

client.connect("mi5.itq.de", port=1883)

counter = 0

while(1):
    print("Test{}".format(counter))
    client.publish("sand.e/test", "Test{}".format(counter))
    counter+=1
    time.sleep(2)