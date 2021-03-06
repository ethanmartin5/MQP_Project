from network import LoRa
import socket
import time
import machine
"""
while True:
    machine.deepsleep(10000)
    machine.sleep(10000, False)
    time.sleep(10)
# Please pick the region that matches where you are using the device
"""
lora = LoRa(mode=LoRa.LORA, region=LoRa.US915)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
while True:
    s.send('Ping')
    print('Ping {}'.format(i))
    i= i+1
    if s.recv(64) == b'Pong':
        print('got a Pong')

    time.sleep(1) # Stops execution of the for loop for X amount of time
