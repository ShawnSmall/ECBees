#!/usr/bin/env python3

#ecb.py

# directory=/home/pi/ECBees



# visual data collection
# make sure start_motion_daemon=yes is in the motion.conf file
 



# temperature data collection with DS18B20
import time

device='sys/bus/w1/devices/28-01191a3cf954/w1_slave'
#                          unique identifier for the thermometer
try:
    while True:
        file = open(device, 'r')
        line = file.readlines()
        file.close()
        t = line[1].find('t=') # find position where 't=' is
        if t :
            temp_val = line[1][t+2:] # grab what's two characters after position
            temp_c = float(temp_val) / 1000.0
            timestamp = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
            print(f'"{timestamp}",{temp_c}') # enclose timestamp (a string) in quotes
            time.sleep(1)
except:
    file.close() # make sure the file is closed
    print("done.")



    # save temperature data to csv file:

import csv

with open('temperature_file.csv', mode='w') as temperature_file:
    temperature_writer = csv.writer(temperature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    temperature_writer.writerow(['Date and Time', 'Temperature',])
    temperature_writer.writerow(['timestamp', 'temp_c ',])


# photoperiod data collection

   # record timestamp for sunrise and for sunset each day:
sunrise = 
sunset = 
date = time.strftime("%Y-%m-%d", time.localtime())

   # save photoperiod data to csv file:
import csv

with open('photoperiod_file.csv', mode='w') as photoperiod_file:
    photoperiod_writer.writerow(['Date', 'Sunrise', 'Sunset',])
    photoperiod_writer.writerow(['date', 'sunrise', 'sunset',])


# vibroacoustic data collection





# shared network program for saving data on remote device





# save data to micro SD card



