#!/usr/bin/env python
import random
'''import RPi.GPIO as GPIO
import time
import keypad_mod, output_mod

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN) #PIR sensor
kp = keypad_mod.keypad()

def readPIR():
    return GPIO.input(21)

def getKeys(kn, prev):
	code = ""
	for c in range(kn):
		time.sleep(0.3)
		key = None
		while key == None:
			key = kp.getKey()
		code += str(key)

		output_mod.printLCD("Enter your", "passcode:" + prev + code)
	time.sleep(0.3)
	return code'''

def readContact():
    entry1 = ['door', 'window', 'doorway']
    status1 = ['open', 'close']

    randomEntry = entry1[random.randint(0,2)]
    randomStatus = status1[random.randint(0,1)]

    return {'entry': randomEntry, 'status': randomStatus}
