
#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

from machine import UART
import machine
import pycom
import os

uart = UART(0, baudrate=115200)
os.dupterm(uart)

# Read in from NV RAM for the next state
key = pycom.nvs_get('test')
print(key)
if key == 0:
    machine.main('initial_state.py')
elif key == 1:
    machine.main('trigger_pong_example.py')
else:
    machine.main('sleep_wait.py')
