import RPi.GPIO as GPIO
import time

LEDpin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDpin,GPIO.OUT)

ON = True
OFF = False

Blink_number = int(input("Enter how many times you want to blink: "))

Blink_delay = float(input("Enter the tiem delay(secdond): "))


for i in range (0,Blink_number):
	GPIO.output(LEDpin,ON)
	time.sleep(Blink_delay)
	GPIO.output(LEDpin,OFF)
	time.sleep(Blink_delay)
	
GPIO.cleanup()
