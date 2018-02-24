import paho.mqtt.client as mqtt
import time

def on_meassage(client, userdata, message):
    print("Message: ", str(message.payload.decode("utf-8")))

print("Start Subscriber")

client_name="nsibfudqnwoezvfnoqwfez33240921"

client = mqtt.Client(client_name)
client.on_meassage=on_meassage
client.connect("mi5.itq.de", port=1883)

client.loop_start()
time.sleep(4)
client.subscribe("sand.e/test")
client.loop_stop()
