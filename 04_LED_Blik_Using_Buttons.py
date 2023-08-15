import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

LED = [37,35,33,31,29]
for i in LED:
    GPIO.setup(i,GPIO.OUT)

inputPin = 40
GPIO.setup(inputPin,GPIO.IN)

try:
	while True:
		readVal = GPIO.input(inputPin)
		print(readVal)
		for i in LED:
			GPIO.output(i,int(readVal))
            
except KeyboardInterrupt:
	GPIO.cleanup()

