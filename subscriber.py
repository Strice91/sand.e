Import paho.mqtt.client as mqtt

print("Start Subscriber")

client_name="nsibfudqnwoezvfnoqwfez33240921"

client = mqtt.Client(client_name)

client.connect(mi5.itq.de, port=1883)

client.subscribe("sand.e/test")
