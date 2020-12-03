#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#this imports the Sensehat library
from sense_hat import SenseHat 
from time import sleep

#creates an object sense
sense = SenseHat() 

red = (252, 177, 3)
sense.show_message("Avik sending info", text_colour = red, scroll_speed = 0.1)
print("Telemetry Packet:")
print(" ")

#Creating an image on the led matrix
X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

question_mark = [
O, O, O, X, X, X, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)

#Collecting RPY Data
#get_orientation a dictionary (a key-value pair) from which you can access corresponding RPY values in degrees
orientation = sense.get_orientation() 
print("pitch: {pitch}".format(**orientation))
print("roll: {roll}".format(**orientation))
print("yaw: {yaw}".format(**orientation))


#Print heading relative to magnetic north but it shuts off gyrocope and accelerometer
#north = sense.get_compass()
#print("North: %s" % north)

#Turn the gyroscope and accelerometer back on
sense.set_imu_config(True, True, True)


#Collecting enviornmental info
#Obtains relative humidity
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity) 

#Gets temperature in degrees celcius
temp = sense.get_temperature()
print("Temperature: %s C" % temp)

#gets pressure in Millibars
pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)
sleep(5)
sense.clear()



# In[2]:


#this libraries
from sense_hat import SenseHat 
from time import sleep
from datetime import datetime
import pandas as pd

#creates an object sense
sense = SenseHat() 

#Create a .csv Telemetry Packet

#Create initial pandas dataframe for sensor data
orientation = sense.get_orientation() 
data = orientation
df = pd.DataFrame([orientation])
#Create a list containing that dataframe
empty_list = [df]

#Create an integer variable i
i = 0

#Create a while loop to continously collect RPY data from SenseHAT
while (i < 20):
    data = sense.get_orientation() 
    empty_list.append(pd.DataFrame([data]))
    sleep(1)
    i += 1

print("Telemetry Packet Stored")

#Save all data frames into the list
result = pd.concat(empty_list, ignore_index = True)
#Set the .csv filename and file_path
file_path = "/home/pi/Desktop/SeniorResearch/TelemetryPackets/TelemetryPacket_" + str(datetime.now()) + ".csv"
#Export data into a csv and safe it to TelemetryPackets
result.to_csv(file_path, index = False)



# In[ ]:


#Camera Script
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.start_preview()
sleep(5)
camera.stop_preview()


# In[ ]:


# Tester
# Checking Roll Pitch Yaw Data
from sense_hat import SenseHat 
sense = SenseHat() 
from time import sleep

while True:
    orientation = sense.get_orientation() 
    print("pitch: {pitch}".format(**orientation))
    print("roll: {roll}".format(**orientation))
    print("yaw: " + str(orientation['yaw'] - 135))
    time.sleep(1)
    


# In[ ]:




