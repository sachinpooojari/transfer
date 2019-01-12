
import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("broker.mqttdashboad",8000,60)
client.publish("topic/sachin", "Hello world!");
client.disconnect();

