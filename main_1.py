

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
j = 0
chrono.start()
sleep = False


# TRANSMIT TO DEVICE FOR 20 SECONDS
while chrono.read() < 20:
    s.send('Ping')
    i=i+1
    print('Ping {}'.format(i))
    # If we establish a connection, then we trasnmit back
    # to the SN 2 that we're going to sleep
    if s.recv(64) == b'Sleep':
        print('We received message from SN2!')
        sleep = True # Triggers the rouotine for longer sleep
        break


# The next loop transmits a message to sensor node 2:
chrono.stop()
chrono.reset()

chrono.start()



# If sleep is true, means that SN2 sent a confirmation message. SN 1 now will send
# Another back to SN 2 confirming it will go to sleep for the allocated time
if sleep == True:
    # Sends a confirmation message for 20 seconds
    while chrono.read() < 20:
        s.send('We got the message')
        j=j+1
        print('Confirmation Message {}'.format(j))
        time.sleep(1)

    # After confirmation is sent, we put it to sleep for 5 minutes
    pycom.nvs_set('test', 0x0002) # Reset for the sleep state
    print('We met the criteria, now reseting')
    machine.reset() # Reset to transition into sleep mode
else:
    # If we aren't going to sleep state, we stay in sensing mode, and go to sleep
    # Until the PIR is triggered again
    pycom.nvs_set('test', 0x0001) # Reset for the sleep state
    print('Sensor Node back to sensing mode (Deep SLeep)')
    machine.deepsleep()
