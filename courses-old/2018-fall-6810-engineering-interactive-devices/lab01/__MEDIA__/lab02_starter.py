#Lab 02 Stater Code

import RPi.GPIO as GPIO
import pygame
import time

#set the pins to be inputs and outputs:
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
inputs = [5,22,27,17]
outputs = [26,19,13,6]
for i in inputs:
    GPIO.setup(i,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for o in outputs:
    GPIO.setup(o,GPIO.OUT)
    GPIO.output(o,0)


#nested list of symbols
symbols = [['1','2','3','A'],
           ['4','5','6','B'],
           ['7','8','9','C'],
           ['*','0','#','D']]

#variable used to remember last symbol pressed (to avoid repeated triggering from holding key)
last_symbol = ''

pygame.mixer.init()
pygame.mixer.music.load('YOUR FILE PATH HERE!!!')
pygame.mixer.music.play()


while True:
    no_symbol_pressed = True
    ##Your Code here!!!  
    time.sleep(0.05)
    if no_symbol_pressed:
        last_symbol = ''
            
