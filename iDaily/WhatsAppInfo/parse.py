from pprint import pprint as ppr
from datetime import datetime

# Global, capitalize
data = []
msgList = []
dtprop = ""

file = open('data.txt', 'r')
DATE_FORMAT = '%I:%M %p, %m/%d/%Y'

# [2:23 PM, 8/2/2021]
# datetime.strptime(dateTime, DATE_FORMAT)

# Make msg holder
# set message Counter

msg = {}
msgCount = 0

for line in file:
	if line.startswith('['):
		if 'txprop' in msg:
			msg['txprop'] = " ".join(msg['txprop'])
			msgList.append(msg)
			msgCount = 0
			msg = {}
		info = line.split("]")
		newDate = info[0]
		newDate = newDate.replace('[', '').replace(']', '').strip()
		dtprop = datetime.strptime(newDate, DATE_FORMAT)
		# msg['ndtprop'] = dtprop
		msg['ndtprop'] = newDate
		msg['txprop'] = [info[1].replace('Dream Freely:', '')]
		# msgList.append(msg)
	elif len(line) == 0:
		print('***\nBLANK LINE\n***')
		continue
	else:
		# Add this message to the message holder
		# msgCount+=1
		# txtVar = 'txtProp' + str(msgCount)
		# msg[txtVar] = line
		msg['txprop'].append(line)

# ppr(msgList)


FmsgList = []
oDate = ""
sMsg = ""

for msg in msgList:
	dtprop = datetime.strptime(msg["ndtprop"], DATE_FORMAT)
	if oDate:
		# If the stored date equals newDate)
		if oDate.day == dtprop.day:
			sMsg["txprop"] = sMsg["txprop"] + msg["txprop"]
			# If the newDate is different?
		else:
			FmsgList.append(sMsg)
			oDate = datetime.strptime(msg["ndtprop"], DATE_FORMAT)
			sMsg = msg
	else:
		oDate = datetime.strptime(msg["ndtprop"], DATE_FORMAT)
		sMsg = msg

import json

with open('output.final.json', 'w+') as f:
    # this would place the entire output on one line
    # use json.dump(lista_items, f, indent=4) to "pretty-print" with four spaces per indent
    json.dump(FmsgList, f)


# Two objects Day, Lesson & Tongue-Twister for the day

# Day Object
# Language
# Level
# Day Number

# Lesson Object
# Topic / Category
# Text in English
# Text in Target Language

# Tongue-Twister Object
# English Text
# Phonetic Text
# Target Language Text

# lastDay = {'ndtprop': datetime.today(), 'txprop': 'hold'}

# for day in msgList:
# 	if lastDay['ndtprop'].date() == day['ndtprop'].date():
# 		# create new Lesson Object
# 	else:
# 		# create new Day & Lesson Object
