#!/usr/bin/env python

import os
import os.path
import time
import thread
import lcd_mod
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
lcd_mod.init()

p = GPIO.PWM(12, 100)

def printLCD(line1, line2):
    print line1, line2
    lcd_mod.lcd_string(line1, LCD_LINE_1)
    lcd_mod.lcd_string(line2, LCD_LINE_2)

def play(path):
    abs_path = os.path.abspath(os.path.join("res", path))
    thread.start_new_thread(os.system, ("mpg123 -q " + abs_path, ))
    time.sleep(0.1)

def playBuzzer(seconds):
    p.start(100)
    p.ChangeDutyCycle(90)
    p.ChangeFrequency(261)
    time.sleep(seconds)
    p.stop()
