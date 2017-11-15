#https://www.hackster.io/hardikrathod/pir-motion-sensor-with-raspberry-pi-415c04
from time import localtime, strftime
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR #pin aanpassen

def Motionlog(status):
    file = open("/home/pi/smarthome/logs/Motionlog", "w")
    file.write(status)
    file.close()
    
try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            #print("Motion Detected...")
            Motionlog(strftime("%d-%m-%Y %H:%M:%S", localtime())) #tijd van detectie
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except: #https://docs.python.org/2/tutorial/errors.html#handling-exceptions
    #http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi
    GPIO.cleanup() 





