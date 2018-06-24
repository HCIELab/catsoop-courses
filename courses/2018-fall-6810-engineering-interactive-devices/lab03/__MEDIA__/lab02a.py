import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Set up GPIO Outputs (LEDs)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.output(4,1)
time.sleep(1)
GPIO.output(17,1)
time.sleep(1)
GPIO.output(27,1)
time.sleep(1)
GPIO.output(4,0)
time.sleep(1)
GPIO.output(17,0)
time.sleep(1)
GPIO.output(27,0)

GPIO.cleanup()