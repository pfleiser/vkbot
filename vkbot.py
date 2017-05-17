# -*- coding: utf-8 -*-
import time
import vk_api

vk = vk_api.VkApi(token='9d303845fdc6c588064a974da6ee46618782c05711c4a90ffe949923acfce59a9c22ce23cdbe516bbbb0d')
vk.auth()

values = {'out': 0,'count': 100,'time_offset': 60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
            write_msg(item[u'user_id'],u'Hi man! Do you want to buy a spinner?')
        else:
            write_msg(item[u'user_id'],u'Sorry, I dont understand you. Try ask again')
    time.sleep(1)