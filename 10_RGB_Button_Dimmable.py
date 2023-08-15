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

DC = 100
freq = 1000

redPWM = GPIO.PWM(REDpin,freq)
greenPWM = GPIO.PWM(GREENpin,freq)
bluePWM = GPIO.PWM(BLUEpin, freq)

redPWM.start(DC)
greenPWM.start(DC)
bluePWM.start(DC)

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
        
        print(red_b_status, redled, blue_b_status, blueled, green_b_status, greenled)
        
        if((red_b_old_status == 1) and (red_b_status == 0)):
            redled = redled *2
            
            if redled < 1:
                redled = 1
            if redled >= DC:
                redled = 0
            
        if((green_b_old_status == 1) and (green_b_status == 0)):
            greenled = greenled *2
            
            if greenled < 1:
                greenled = 1
            if greenled >= DC:
                greenled = 0
            
        if((blue_b_old_status == 1) and (blue_b_status == 0)):
            blueled = blueled *2
            
            if blueled < 1:
                blueled = 1
            if blueled >= DC:
                blueled = 0
        
        redPWM.ChangeDutyCycle(redled)
        bluePWM.ChangeDutyCycle(blueled)
        greenPWM.ChangeDutyCycle(greenled)
        
        
        red_b_old_status = red_b_status
        green_b_old_status = green_b_status
        blue_b_old_status = blue_b_status
        
except KeyboardInterrupt:
	GPIO.cleanup()
	redPWM.stop()
	greenPWM.stop()
	bluePWM.stop()
	print("GPIO is good to go")

