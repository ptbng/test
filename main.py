# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:19:18 2023

@author: 84908
"""

import sys
from Adafruit_IO import MQTTClient
import time
import random
from eval_testing import *
import requests

print("AIoT Project")
AIO_FEED_IDs = ["nutnhan1", "nutnhan2", "equation"]
AIO_USERNAME = "ptbngoc"
AIO_KEY = "aio_VbtU307yoO725YBvEzxfKcdMnQry"
global_equation = ""

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)
    
def subcribe(client, userdata, mid, granted_qos):
    print("Subcribe thanh cong ...")
    
def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)
    
def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload + " , feed id: " + feed_id)
    if(feed_id == "equation"):
        global_equation = payload
        print(global_equation)
        
def init_global_equation():
    headers = {}
    aio_url = 'https://io.adafruit.com/api/v2/ptbngoc/feeds/equation'
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()
    global_equation = data["last_value"]
    print("Get lastest value:", global_equation)

    
client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subcribe
client.connect()
client.loop_background()
counter = 10
sensor_type = 0
while True:
    #counter = counter - 1
    #if counter <= 0:
        #counter = 10
        #TODO
        #print("Random data is publishing ...")
        #if sensor_type == 0:
            #print("Tempurature  ...")
            #temp = random.randint(10, 20)
            #client.publish("cambien1", temp)
            #sensor_type = 1
        #elif sensor_type == 1:
            #print("Humidity ...")
            #humi = random.randint(50, 70)
            #client.publish("cambien2", humi)
            #sensor_type = 2
        #elif sensor_type == 2:
            #print("Light ...")
            #light = random.randint(100, 500)
            #client.publish("cambien3", light)
            #sensor_type = 0
    init_global_equation()    
    x1 = random.randint(3, 9)
    x2 = random.randint(10, 19)
    x3 = random.randint(20, 29)
    global_equation = modify_value(x1, x2, x3)
    client.publish("equation1", global_equation)
    time.sleep(1)
    pass

