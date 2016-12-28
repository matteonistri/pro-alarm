#!/usr/bin/env python

import input_mod, output_mod, keypad_mod
import slackbot
import time
from datetime import datetime
import threading, os, thread

STATUS = "OFF"
PASSCODE = "1245"
DELAY = 10

def controlTower():
    global STATUS
    kp = keypad_mod.keypad()

    output_mod.printLCD("System OFF", str(datetime.now())[:16])

    while True:
        if kp.getKey() is not None:
			requestPasscode(kp.getKey())
        
        if STATUS == "ON":
            if input_mod.read433() is not None:
                alert()
        
        time.sleep(0.1)

def requestPasscode(key):
    output_mod.printLCD("Enter your", "passcode:" + str(key))
    code = str(key) + input_mod.getKeys(3, str(key))

    if not checkPasscode(code):
        output_mod.printLCD("Wrong passcode", "")
        time.sleep(1)
        output_mod.printLCD("System " + STATUS, str(datetime.now())[:16])

def checkPasscode(code):
    global STATUS
    global PASSCODE

    if code == PASSCODE:
        if STATUS == "ON":
            STATUS = "OFF"
            output_mod.printLCD("System OFF", str(datetime.now())[:16])
            output_mod.playBuzzer(0)
            os.system("pkill mpg123")

        else:
            STATUS = "ON"
            thread.start_new_thread(output_mod.playBuzzer, (DELAY,))
            for i in range(DELAY, 0, -1):
                output_mod.printLCD("Turning on...", "%d seconds" % i)
                time.sleep(1)
            output_mod.printLCD("System ON", str(datetime.now())[:16])

        return True
    return False

def alert():
    timer = threading.Timer(DELAY, onAlarm)
    timer.start()
    thread.start_new_thread(output_mod.playBuzzer, (DELAY,))

    while True:
        output_mod.printLCD("Enter your", "passcode:")
        att = input_mod.getKeys(4, "")
        if checkPasscode(att):
            timer.cancel()
            break

def onAlarm():
	output_mod.play("alarm.mp3")
	slackbot.sendMessage();

if __name__ == "__main__":
    controlTower()
