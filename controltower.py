#!/usr/bin/env python

import input_mod, output_mod, keypad_mod
import slackbot
import time
from datetime import datetime
import threading, os, thread

STATUS = "ON"
PASSCODE = "1245"


def controlTower():
    global STATUS
    #output_mod.play("armed.mp3")
    kp = keypad_mod.keypad()
    print datetime.now()
    output_mod.printLCD("System ON", str(datetime.now())[:16])
    while True:
        move = input_mod.readPIR()
        print datetime.now(), "[CONTROLTOWER]", move
        if STATUS == "ON":
            if move == 1:
                alert()

        if kp.getKey() != None:
			requestPasscode(kp.getKey())

        time.sleep(0.1)

def requestPasscode(key):
    output_mod.printLCD("Enter your", "passcode:" + str(key))
    code = str(key) + input_mod.getKeys(3, str(key))

    if not checkPasscode(code):
        output_mod.printLCD("Wrong passcode", "")
        time.sleep(2)
        output_mod.printLCD("System " + STATUS, str(datetime.now())[:16])

def onAlarm():
	output_mod.play("alarm.mp3")
	slackbot.sendMessage();

def alert():
    timer = threading.Timer(10.0, onAlarm)
    timer.start()
    #output_mod.play("movement.mp3")
    thread.start_new_thread(output_mod.playBuzzer, (10,))

    while True:
        output_mod.printLCD("Enter your", "passcode:")
        att = input_mod.getKeys(4, "")
        if checkPasscode(att):
            timer.cancel()
            break

def checkPasscode(code):
    global STATUS

    if code == PASSCODE:
        if STATUS == "ON":
            STATUS = "OFF"
            output_mod.printLCD("System OFF", str(datetime.now())[:16])
            output_mod.playBuzzer(0)
            os.system("pkill mpg123")
            #output_mod.play("disarmed.mp3")

        else:
            STATUS = "ON"
            output_mod.printLCD("Turning on...", "10 seconds")
            output_mod.playBuzzer(10)
            output_mod.printLCD("System ON", str(datetime.now())[:16])
            time.sleep(10)
            #output_mod.play("armed.mp3")

        return True
    return False

if __name__ == "__main__":
    controlTower()
