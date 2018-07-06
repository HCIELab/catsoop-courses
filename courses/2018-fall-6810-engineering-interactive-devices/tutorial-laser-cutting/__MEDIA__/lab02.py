#Lab 02 Stater Code

import RPi.GPIO as GPIO
import pygame
import time

#set
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
inputs = [5,22,27,17]
outputs = [26,19,13,6]
for i in inputs:
    GPIO.setup(i,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for o in outputs:
    GPIO.setup(o,GPIO.OUT)
    GPIO.output(o,0)

symbols = [['1','2','3','A'],
           ['4','5','6','B'],
           ['7','8','9','C'],
           ['*','0','#','D']]

last_symbol = ''

pygame.mixer.init()
pygame.mixer.music.load('YOUR FILE PATH HERE!!!')
pygame.mixer.music.play()


while True:
    all_clear = True
    for o in range(len(outputs)):
        GPIO.output(outputs[o],1)
        for i in range(len(inputs)):
            if GPIO.input(inputs[i]):
                all_clear = False
                if last_symbol != symbols[o][i]:
                    last_symbol = symbols[o][i]
                    print(symbols[o][i])
                    if last_symbol == "A":
                        pygame.mixer.music.pause()
                    if last_symbol == "B":
                        pygame.mixer.music.unpause()
                    if last_symbol in ['0','1','2','3','4','5','6','7','8','9']:
                        pygame.mixer.music.set_volume(float(last_symbol)/10.0) 
        GPIO.output(outputs[o],0)
    time.sleep(0.05)
    if all_clear:
        last_symbol = ''
            
