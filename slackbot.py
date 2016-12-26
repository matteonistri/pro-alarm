#!/usr/bin/env python
import os
from datetime import datetime
import time
from slackclient import SlackClient

BOT_ID = os.getenv('BOT_ID')
slack_client = SlackClient(os.getenv('SLACK_BOT_TOKEN'))

def sendMessage():
	now = datetime.now()
	response = "alarm activated at " + str(now)
	slack_client.api_call("chat.postMessage", channel='general', text=response, as_user=True)
	print now, "[SLACKBOT] message sent"
