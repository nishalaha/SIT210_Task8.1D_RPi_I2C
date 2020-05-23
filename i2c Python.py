#referenced :https://www.thegeekpub.com/18263/raspberry-pi-to-arduino-i2c-communication/

import RPi.GPIO as GPIO
from smbus import SMBus

address = 0x8 #bus address 
bus = SMBus(1) #indicates /dev/i2c-1

print ("Type 1 for led to ON and 0 to OFF")
try:
 while True:

    value = input ("Value :  ")
    
    if value == "1":
        bus.write_byte(address, 0x1) #switch on
    elif value == "0":
        bus.write_byte(address, 0x0) #switch off

except KeyboardInterrupt:
   GPIO.cleanup()   