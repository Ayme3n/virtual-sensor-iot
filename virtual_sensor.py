import json
import paho.mqtt.client as mqtt
import time
import random

THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'fSX3UTA5EzMcT10s8T6R'

# Callback for incoming RPC commands
def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(f"RPC command received: {payload}")
    try:
        data = json.loads(payload)
        if "fan_state" in data:
            print(f"Setting fan_state to: {data['fan_state']}")
    except:
        print("Invalid command format")

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.on_message = on_message
client.subscribe('v1/devices/me/rpc/request/+')
client.loop_start()

while True:
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 60), 2)
    payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'
    client.publish('v1/devices/me/telemetry', payload)
    print(f"Sent: {payload}")
    time.sleep(5)
