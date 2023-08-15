import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = [37,35,33,31,29]
for i in LED:
    GPIO.setup(i,GPIO.OUT)

try:
    while True:
        for i in LED:
            GPIO.output(i,True)
        time.sleep(0.3)
        for i in LED:
            GPIO.output(i,False)
        time.sleep(0.3)
except KeyboardInterrupt:
    GPIO.cleanup()

