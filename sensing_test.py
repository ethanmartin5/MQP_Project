
import time
from machine import Pin

pir = Pin('P4',mode=Pin.IN, pull=Pin.PULL_UP)


# main loop
print("Starting main loop")
while True:
    if pir() == 1:
        print('Presence Detected ')

    else:
        last_trigger = 0
        print("No presence")

    time.sleep_ms(50)

print("Exited main loop")
