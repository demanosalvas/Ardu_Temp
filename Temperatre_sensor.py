# Imports
import serial
import time
import numpy
import ftplib
import os
import requests

# Open serial port
ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
time.sleep(1)
ser.flush()

# Setup dweet.io variables
dweetIO = "https://dweet.io/dweet/for/"
myName = "ambienttemperature1234"
myKey = "measure_temp"  

# Can be read at:
# http://dweet.io/follow/ambienttemperature1234

# Trash the first data
for i in range(2):
    ser.readline()

# Main loop
while(True):

    # Read data and convert to temperature 
    temp = int(9./5*(((int(ser.readline())*0.004882814) - 0.5) * 100) +32)
    #temp = numpy.random.randint(60, 90)
    print temp
    
    #Send to Cloud, dweet.io
    rqsString = dweetIO+myName+'?'+myKey+'='+str(temp)
    print(rqsString)
    rqs = requests.get(rqsString)
    print rqs.status_code
    print rqs.headers
    print rqs.content    