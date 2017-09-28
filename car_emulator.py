import random
import time

class Car:

    client = None

    vin = ""
    error_array = []
    fuel = 1
    longitude = 0.0
    latitude = 0.0

    time = 0

    delta = 0.000001
    delta_increment = 0.00001

    fuel_delta = 0.001
    def __init__(self,vin,x,y,time,client,errors):
        self.longitude = y
        self.latitude = x
        self.time = time
        self.client = client
        self.vin = vin
        self.error_array = errors

    def drive_up(self):
        self.longitude += self.delta
        self.fuel -= self.fuel_delta
        self.send_stat()
    def drive_left(self):
        self.latitude -= self.delta
        self.fuel -= self.fuel_delta
        self.send_stat()
    def drive_down(self):
        self.longitude -= self.delta
        self.fuel -= self.fuel_delta
        self.send_stat()
    def drive_right(self):
        self.latitude += self.delta
        self.fuel -= self.fuel_delta
        self.send_stat()

    def drive_araund(self):
        while(self.fuel>0):

            self.time += 1
            self.drive_left()
            time.sleep(0.1)
            self.time += 1
            self.drive_down()
            time.sleep(0.1)
            self.time += 1
            self.delta += self.delta_increment
            self.drive_right()
            time.sleep(0.1)
            self.time += 1
            self.drive_up()
            time.sleep(0.1)

    def send_stat(self):
        self.send_stat_1()
        self.send_stat_2()
        self.send_stat_3()
        self.send_stat_4()

    def send_stat_1(self):
        msg = ""
        msg += self.vin + "_"
        msg += "1_"
        msg += str(self.time)+"_"

        for error in self.error_array:
            msg+=error+"_"
        print(msg)
        self.client.publish("mts_hardware_get_info_chanel",msg)

    def send_stat_2(self):
        msg = ""
        msg += self.vin + "_"
        msg += "2_"
        msg += str(self.time)+"_"

        msg += str(random.randrange(0, 1000) / 1000.0) + "_"
        msg += str(random.randrange(0, 1000) / 1000.0) + "_"
        msg += str(random.randrange(0, 8000))
        print(msg)
        self.client.publish("mts_hardware_get_info_chanel",msg)

    def send_stat_3(self):
        msg = ""
        msg += self.vin + "_"
        msg += "3_"
        msg += str(self.time)+"_"

        msg += str(random.randrange(10, 130)) + "_"
        msg += str(self.latitude) + "_"
        msg += str(self.longitude)
        print(msg)
        self.client.publish("mts_hardware_get_info_chanel",msg)

    def send_stat_4(self):
        msg = ""
        msg += self.vin + "_"
        msg += "4_"
        msg += str(self.time) + "_"
        msg += str(self.fuel) + "_"
        msg += str(random.randrange(0, 1000) / 100.0) + "_"
        msg += str(random.randrange(0, 1000) / 100.0) + "_"
        msg += str(random.randrange(0, 1000) / 100.0)
        print(msg)
        self.client.publish("mts_hardware_get_info_chanel",msg)

