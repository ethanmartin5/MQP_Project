from network import LoRa
import socket
import time
import machine



import time
from machine import Pin

print("Welcome to the sleep State! We'll be right back")

# Set the integer to transition back into listening mode
#pycom.nvs_set('test', 0x0000)
pycom.nvs_set('test', 0x0000)
print("We've just changed the ram value, now going to sleep..")

# IF IT READS IN FROM THE LORA, THEN IT WILL STAY IN SLEEP MODE FOR A SET PERIOD OF
# TIME, i.e. 5 or so minutes:
minutes = 0.01
ms_sleep = int(minutes * 60000) # 60000 ms per minute

machine.deepsleep(ms_sleep)
