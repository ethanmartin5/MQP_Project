
from machine import Timer
import time
import machine
from machine import Pin
from network import LoRa
import socket


chrono = Timer.Chrono()

# Initialize LoRa Socket:
lora = LoRa(mode=LoRa.LORA, region=LoRa.US915)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0

import time
from machine import Pin

pir = Pin('P4',mode=Pin.IN, pull=Pin.PULL_UP)
machine.pin_sleep_wakeup([pir], machine.WAKEUP_ANY_HIGH, False)


chrono.start()
active = False
print('I woke up')
# Begin reading if SN 1 has sent a message
print('Reading..')


while chrono.read() < 20:
    if s.recv(64) == b'Ping':
        # Debugging statements
        print('Sensor Node 1 Activated')
        print('Sending confirmation to SN1')
        active = True
        break
    time.sleep(1)



print('Sensor Node back to sensing mode (Deep Sleep)')
machine.deepsleep()
