import paho.mqtt.client as mqtt
from car_emulator import *
client = mqtt.Client("mts_hardware_get_info_chanel_spammer")
client.connect("broker.hivemq.com")


car1 = Car("1D4GP00R55B123456",1,1,0,client,["p1","p2"])
car1.drive_araund()
#client.publish("mts_hardware_get_info_chanel",1)