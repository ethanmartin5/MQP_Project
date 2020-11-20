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
    s.send('Send')
    i=i+1
    print('Send {}'.format(i))
    # If we establish a connection, then we trasnmit back
    # to the SN 2 that we're going to sleep
    if s.recv(64) == b'Sleep':
        print('\nWe received message from SN2!')

        sleep = True # Triggers the rouotine for longer sleep
        break
    time.sleep(1)

# The next loop transmits a message to sensor node 2:
chrono.stop()
chrono.reset()

chrono.start()



# If sleep is true, means that SN2 sent a confirmation message. SN 1 now will send
# Another back to SN 2 confirming it will go to sleep for the allocated time
if sleep == True:
    # Sends a confirmation message for 20 seconds
    print('Sending confirmation message\n')
    while chrono.read() < 10:
        s.send('Confirmed')
        j=j+1
        print('Confirmed {}'.format(j))
        time.sleep(1)

    # After confirmation is sent, we put it to sleep for 5 minutes
    pycom.nvs_set('test', 0x0010) # Reset for the sleep state
    print('criteria met, sleeping')
    machine.reset() # Reset to transition into sleep mode
else:
    # If we aren't going to sleep state, we stay in sensing mode, and go to sleep
    # Until the PIR is triggered again
    print('Sensor Node back to sensing mode (Deep SLeep)')
    machine.deepsleep()
