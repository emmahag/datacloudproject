#receivedatafromMQTT
import paho.mqtt.client as mqtt
from ..step4.step4 import filterNotification
from ..step3.step3 import createNotification

host="localhost"
port=1883

timelive=60

def on_message(client, userdata, msg):
    print(msg.payload.decode())
    createNotification(filterNotification(msg))
    
    
def on_connect(client, userdata, flags, rc):
  print("Connected")
  client.subscribe("/Data")
  

client = mqtt.Client()
client.connect(host,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()