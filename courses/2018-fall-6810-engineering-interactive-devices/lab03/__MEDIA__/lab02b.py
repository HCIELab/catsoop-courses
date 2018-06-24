import RPi.GPIO as GPIO
import time

#setup pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pins = [4,17,27] #need to add pin 5!
for pin in pins:
	GPIO.setup(pin,GPIO.OUT)

GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP) #set up pin 24 as an input.
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP) #set up pin 24 as an input.
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_UP) #set up pin 24 as an input.


try:
	while True:
		#your code here
		time.sleep(0.1)

except:
   GPIO.cleanup()

GPIO.cleanup()