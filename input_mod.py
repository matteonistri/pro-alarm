#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import keypad_mod, output_mod
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN) #PIR sensor
kp = keypad_mod.keypad()

def readPIR():
    return GPIO.input(21)

def read433():
	ser.flushInput()
	line = ser.readline()
	words = line.split(" ")
	print words[1]
	return words[1]
    
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
