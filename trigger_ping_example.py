

# CODE FOR Sensor node 1

from machine import Timer
import time
import machine
from machine import Pin
from network import LoRa
import socket


chrono = Timer.Chrono()


pir1 = Pin('P4',mode=Pin.IN, pull=Pin.PULL_UP)
machine.pin_sleep_wakeup([pir1], machine.WAKEUP_ANY_HIGH, False)

print('I woke up')

# Initialize LoRa Socket:
lora = LoRa(mode=LoRa.LORA, region=LoRa.US915)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
sleep = False


# TRANSMIT TO DEVICE FOR 20 SECONDS
while i < 20:
    s.send('Ping')
    i=i+1
    print('Ping {}'.format(i))
    # If we establish a connection, then we trasnmit back
    # to the SN 2 that we're going to sleep
    if s.recv(64) == b'Sleep':
        print('We received message from SN2!')
        sleep = True # Triggers the rouotine for longer sleep
        break
    time.sleep(1)


pycom.nvs_set('test', 0x0001) # Reset for the sleep state
print('Sensor Node back to sensing mode (Deep SLeep)')
machine.deepsleep()
