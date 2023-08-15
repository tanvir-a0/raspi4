import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

LED = [37,35,33,31,29]
for i in LED:
    GPIO.setup(i,GPIO.OUT)

inputPin = 40
GPIO.setup(inputPin,GPIO.IN)


oldButtonValue = 0
newButtonValue = 0
status = 0

try:
	while True:
		newButtonValue = GPIO.input(inputPin)
		sleep(0.05)
		print("oldButtonValue = " + str(oldButtonValue) + " status = " + str(status))
		
		if((oldButtonValue == 0) and (newButtonValue == 1)):
			if status == 0:
				status = 1
			else:
				status = 0
				
		oldButtonValue = newButtonValue 
		
		for i in LED:
			GPIO.output(i,int(status))
            
except KeyboardInterrupt:
	GPIO.cleanup()

