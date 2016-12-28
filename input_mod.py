#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import keypad_mod, output_mod
import serial
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN) #PIR sensor
kp = keypad_mod.keypad()

def readPIR():
    return GPIO.input(21)

def read433():
	ser.flushInput()
	line = ser.readline()
	if not line == "":
		words = line.split(" ")
		print datetime.now(), "[433RECEIVER] received ", words[1]
		return words[1]
	return None
    
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
	return code
