#!/usr/bin/env python
import os
from datetime import datetime
import time
from slackclient import SlackClient

slack_client = SlackClient(os.getenv('SLACK_BOT_TOKEN'))

def sendMessage():
	now = datetime.now()
	msg = "alarm activated at " + str(now)
	response = slack_client.api_call("chat.postMessage", channel='general', text=msg, as_user=True)
	if response["ok"]:
		print now, "[SLACKBOT] message sent"
	else:
		print now, "[SLACKBOT] error occurred. message not sent"

