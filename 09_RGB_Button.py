import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

REDpin = 35
GREENpin = 37
BLUEpin = 33

GPIO.setup(REDpin, GPIO.OUT)
GPIO.setup(GREENpin, GPIO.OUT)
GPIO.setup(BLUEpin, GPIO.OUT)

red_b_pin = 40
green_b_pin = 36
blue_b_pin = 38

GPIO.setup(red_b_pin,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(green_b_pin,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(blue_b_pin,GPIO.IN, pull_up_down = GPIO.PUD_UP)

red_b_status = 1
green_b_status = 1
blue_b_status = 1

red_b_old_status = 1
green_b_old_status = 1
blue_b_old_status = 1

greenled = 0
redled = 0
blueled = 0

try:
    while True:
        red_b_status = GPIO.input(red_b_pin)
        blue_b_status = GPIO.input(blue_b_pin)
        green_b_status = GPIO.input(green_b_pin)
        
        print(red_b_status, blue_b_status, green_b_status)
        
        if((red_b_old_status == 1) and (red_b_status == 0)):
            if redled == 0:
                redled = 1
            else:
                redled = 0
            
        if((green_b_old_status == 1) and (green_b_status == 0)):
            if greenled == 0:
                greenled = 1
            else:
                greenled = 0
            
        if((blue_b_old_status == 1) and (blue_b_status == 0)):
            if blueled == 0:
                blueled = 1
            else:
                blueled = 0
        
        GPIO.output(REDpin,redled)
        GPIO.output(GREENpin,greenled)
        GPIO.output(BLUEpin,blueled)
        
        
        red_b_old_status = red_b_status
        green_b_old_status = green_b_status
        blue_b_old_status = blue_b_status
        
except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO is good to go")

