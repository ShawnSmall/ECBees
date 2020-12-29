#!/usr/bin/env python3

# directory=/home/pi/ECBees



# visual data collection
# make sure start_motion_daemon=yes is in the motion.conf file
sudo motion



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

# vibroacoustic data collection





# shared network program for saving data on remote device





# save data to micro SD card
