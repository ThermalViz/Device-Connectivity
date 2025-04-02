import RPi.GPIO as GPIO
import time
import os

os.system("sudo systemctl start nginx")

inCH1 = 17
inCH2 = 27
inCH3 = 22
inCH4 = 23
outCH = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(inCH1, GPIO.IN)
GPIO.setup(inCH2, GPIO.IN)
GPIO.setup(inCH3, GPIO.IN)
GPIO.setup(inCH4, GPIO.IN)
GPIO.setup(outCH, GPIO.OUT)

counter = 0
status = GPIO.LOW

print("Sensor Reading...")

def convert(x):
    if (x == 1):
        return "HIGH"
    else:
        return "LOW"
    
while (True):
    #Write data to file in CSV format
    with open ('/var/www/html/data.csv','w') as datafile:
        
        readings = [convert(GPIO.input(inCH1)) + ",", convert(GPIO.input(inCH2)) + ",", convert(GPIO.input(inCH3))  + ",", convert(GPIO.input(inCH4)) + ",", convert(status)]
        datafile.writelines(readings)    
        
        
    #Blink LED
    GPIO.output(outCH, status)
    
    counter += 1
    
    if (counter >= 4):
        counter = 0
        
        if (status == GPIO.LOW):
            status = GPIO.HIGH
        else:
            status = GPIO.LOW
    
    
            
    
    time.sleep(1.0)

  
