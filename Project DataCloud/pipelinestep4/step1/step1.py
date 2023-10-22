#generatesampledata
import paho.mqtt.client as paho
from faker import Faker
import random
import time

host="localhost"
port = 1883

def publish(client,userdata,result):
    print("Published data")

client= paho.Client("admin")
client.on_publish = publish
client.connect(host, port)

fake = Faker()
sampledata = []
N = 20
for i in range(N):
    sampledata.append([fake.name(), fake.email()])

print(sampledata)
ret = client.publish("/Data", sampledata)