import RPi.GPIO as GPIO
from time import sleep

freq = 1000

dt = 0.1 #delay time seconds
b1 = 40
b2 = 38

b1state = 1
b1stateold = 1

b2state =1
b2stateold = 1

LEDPin = 37
DC = 9

GPIO.setmode(GPIO.BOARD)
GPIO.setup(b1,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(b2,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LEDPin, GPIO.OUT)

myPWM = GPIO.PWM(LEDPin,freq)
myPWM.start(DC)


try:
	while True:
		b1state = GPIO.input(b1)
		b2state = GPIO.input(b2)
		
		#print(b1state, b2state)
		
		if b1state == 0 and b1stateold == 1 :
			DC = DC * 2 + (DC == 0)
			
			print("Intcreasing Brightness")
		
		if b2state == 0 and b2stateold == 1 :
			DC = DC / 2
			print("Decreasing Brightness")
		
		DC = int(DC)
		#print(DC)
		
		if DC > 99:
			DC = 99
		
		if DC < 0: 
			DC = 0
			
		myPWM.ChangeDutyCycle(DC)
		
		b1stateold = b1state
		b2stateold = b2state
	
	
except KeyboardInterrupt:
	myPWM.stop()
	GPIO.cleanup()
	print("GPIO is good to go")

