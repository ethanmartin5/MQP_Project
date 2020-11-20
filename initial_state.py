
from network import LoRa
import socket
import time
import machine


from machine import Pin

print('Welcome to the initial sleep state')
# Assign the next state to sensing mode
pycom.nvs_set('test', 0x0001)
pir1 = Pin('P4',mode=Pin.IN, pull=Pin.PULL_UP)
machine.pin_sleep_wakeup([pir1], machine.WAKEUP_ANY_HIGH, False)

machine.deepsleep()
