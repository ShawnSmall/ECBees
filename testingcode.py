#! /usr/bin/env python3

#a = "hello\n" # \n is a newline character
#b = "world"
#a = a.strip() # this removes white space from both ends
#print(f'{a} to the whole {b}.')
#file = open("testing.csv","a",buffering=1)
#file.write(f'{a} to the whole {b}.')
#file.close()


import time
#import csv
device='/sys/bus/w1/devices/28-01191a3cf954/w1_slave'

try:
    while True:
        file = open(device, 'r')
        line = file.readlines()
        file.close
        t = line[1].find('t=') # find the position where 't=' is
        if t:
            temp_val = line[1][t+2:] #grab what's two characters after position
            temp_c = float(temp_val) / 1000.0
            timestamp = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
            print(f'"{timestamp}",{temp_c}') #enclose timestamp (a string) in quotes
            time.sleep(10) #record the temperature every 10 seconds
except:
    file.close() #make sure the file is closed
    print("done.")


#            file = open('temperature.csv','a',buffering=1)
#            file.write(f'{timestamp},{temp_c},')
#            file.close()

#csv.writer(temperature.csv, delimiter=',', quotechar='"', quoting=$


#import csv

#with open('temperature_file.csv', mode='w') as temperature_file:
#    temperature_writer = csv.writer(temperature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#    temperature_writer.writerow(['Date and Time', 'Temperature',])
#    temperature_writer.writerow(['timestamp', 'temp_c',])
#file.close()

