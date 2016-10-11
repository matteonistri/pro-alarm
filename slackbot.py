#!/usr/bin/env python
import os
from datetime import datetime
import time
from slackclient import SlackClient

BOT_ID = 'U2M5LADFS'
slack_client = SlackClient('xoxb-89190353536-cjxR3GJaynkzmmZjUghzv2rB')

def sendMessage():		
	now = datetime.now()
	response = "alarm activated at " + str(now)
	slack_client.api_call("chat.postMessage", channel='general', text=response, as_user=True)
	print "message sent"
