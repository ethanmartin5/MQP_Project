

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
    print('Reading')
    if s.recv(64) == b'Ping':

        # Debugging statements
        print('Sensor Node 1 Activated')
        print('Sending confirmation to SN1')
        active = True
        break

# If active is True, we can transmit to the SN1 telling it to shut down:

# The next loop transmits a message to sensor node 2:

# STOP, RESET, and RESTART timer
chrono.stop()
chrono.reset()
chrono.start()

# If we're active, we transmit to SN1 to shut off
sleep = False
if active == True:
    while chrono.read() < 20:
        s.send('Sleep')
        i=i+1
        print('Sleep {}'.format(i))
        # If we establish a connection, then we trasnmit back
        # to the SN 2 that we're going to sleep
        if s.recv(64) == b'Confirm':
            print('SN1 going to sleep!')
            # Read the SN1 sleep count from memory
            count = pycom.nvs_get('SN1_sleep')
            count = int(count) + 1
            pycom.nvs_set('SN1_sleep', hex(count))
            break
        time.sleep(1)

    # Now that we've confirmed sleep, it's time to transmit to the camera
    # node, and wait to see that we got the message:
    chrono.stop()
    chrono.reset()
    chrono.start()

    # Send message to CN
    while chrono.read() < 20:
        s.send('Motion_Detected')
        i=i+1
        print('Sleep {}'.format(i))
        # If we establish a connection, then we trasnmit back
        # to the SN 2 that we're going to sleep
        if s.recv(64) == b'Confirm':
            print('Confirmed')
            print('Getting ready for sleep')
            camera = True
            break
        time.sleep(1)
# If we haven't gotten anything from sensor node 1, we just continue




# STOP, RESET, and RESTART timer
chrono.stop()
chrono.reset()
chrono.start()
camera = False
# If we've confirmed from the Camera node, then we'll get ready for sleep
if sleep == True:
    if camera == True:
    # Sends a confirmation message for 20 seconds
        while chrono.read() < 20:
            s.send('We got the message')
            j=j+1
            print('Confirmation Message {}'.format(j))
            time.sleep(1)

    # After confirmation is sent, we put it to sleep for 5 minutes
    pycom.nvs_set('test', 0x0000) # Reset for the sleep state
    print('We met the criteria, now reseting')
    machine.reset() # Reset to transition into sleep mode
else:
    print('Sensor Node back to sensing mode (Deep Sleep)')
    machine.deepsleep()
