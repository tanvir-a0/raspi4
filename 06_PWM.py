import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)

GPIO.output(37,True)
GPIO.output(37,False)
GPIO.output(37,True)
GPIO.output(37,False)

myPWM = GPIO.PWM(37,1000)
myPWM.start(50)
try:
    while(1):
        t = 0.08
        myPWM.ChangeDutyCycle(99)
        time.sleep(t)
        myPWM.ChangeDutyCycle(80)
        time.sleep(t)
        myPWM.ChangeDutyCycle(60)
        time.sleep(t)
        myPWM.ChangeDutyCycle(50)
        time.sleep(t)
        myPWM.ChangeDutyCycle(40)
        time.sleep(t)
        myPWM.ChangeDutyCycle(30)
        time.sleep(t)
        myPWM.ChangeDutyCycle(20)
        time.sleep(t)
        myPWM.ChangeDutyCycle(10)
        time.sleep(t)
        myPWM.ChangeDutyCycle(1)
        time.sleep(t)
        

except KeyboardInterrupt:
    GPIO.cleanup()
