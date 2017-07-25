#!/usr/bin/env python

import telepot
import time
import requests
import os

HOST = "127.0.0.1"
PORT = 8050

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('')
    print(time.strftime('[%d %b, %y %r] ' + str(chat_id) + ': ' + command))

	command = command.replace(' --force', '')
	bot.sendChatAction(chat_id, 'typing')

	if command == '/start':
		bot.sendMessage(chat_id, 'Starting Kodi')
		os.system('kodi &')
	elif command == '/stop':
		bot.sendMessage(chat_id, 'Sending kill signal')
		os.system('pkill -f kodi')
	else:
		data = '[{"jsonrpc":"2.0","method":"Input.SendText","params":["' + command + '"],"id":10}]'
		requests.post('http://{0}:{1}/jsonrpc?Input.SendText'.format(HOST, PORT), data=data)
		bot.sendMessage(chat_id, 'Text sent')

bot = telepot.Bot('I_NEED_TOKEN!')
bot.message_loop(handle)
print('I am listening ...')

while True:
    time.sleep(10)
