# -*- coding: utf-8 -*-
# Chat bot for VK page of Spinn.ee webshop.

import time
import vk_api


def check(test): #Rewrites the function and starts using code below
    if test == "Hi":  # Check if response correct zdes zamena
        return "Hi man! Do you want to buy a spinner? If yes, type 1."
    elif test == '1':
        return "Great idea! Do you thought which material do you like the most? Maybe, plastic or metal? Type it."
    elif test == 'plastic':
        return "Plastic does not mean cheap! Tell me, what cost do you want a spinner? Type 5, 9 or 10."
    elif test == '5':
        return "Wow, dude, look what you found! Spinner like you wanted - plastic and for 5 euros. Wait, but the color? Type black, blue or white."
    elif test == 'blue':
        return "Fuh, it was not easy, but I found it. Blue plastic spinner for 5 euros. Come to our site and buy it. Right now. JUST DO IT! http://spinn.ee/toode/spinner-1/"
    elif test == 'black':
        return "Fuh, it was not easy, but I found it. Black plastic spinner for 5 euros. Come to our site and buy it. Right now. JUST DO IT! http://spinn.ee/toode/spinner-1/"
    elif test == 'white':
        return "Fuh, it was not easy, but I found it. White plastic spinner for 5 euros. Come to our site and buy it. Right now. JUST DO IT! http://spinn.ee/toode/spinner-1/"
    else:
         return "Sorry, I dont understand you. Try ask again"

def start():
    # We're using special token code which you can find in VK page setting
    vk = vk_api.VkApi(token='77196449c7b26ffa9777e3c9e85b85debc05108dae9a672c6bcbb8468a1efa66fd06e4d947aa8ab24745e')
    vk.auth()

    # Time debuggig (attempt to humanize the bot)
    values = {'out': 0,'count': 100,'time_offset': 60}

    def write_msg(user_id, s):
        vk.method('messages.send', {'user_id':user_id,'message':s})


    # If user starts writing something, bot understand that and ready to answer after the message.

    while True:
        response = vk.method('messages.get', values)
        if response['items']:
            values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:
            if check(response['items'][0]['body']): #Check if response correct zdes zamena
                write_msg(item[u'user_id'], u'Hi man! Do you want to buy a spinner? If yes, type 1.')
#               return "Hi man! Do you want to buy a spinner? If yes, type 1."
            elif response['items'][0]['body'] == '1':
                write_msg(item[u'user_id'],u'Great idea! Do you thought which material do you like the most? Maybe, plastic or metal? Type it.')
            elif response['items'][0]['body'] == 'plastic':
                write_msg(item[u'user_id'],u'Plastic does not mean cheap! Tell me, what cost do you want a spinner? Type 5, 9 or 10.')
            elif response['items'][0]['body'] == '5':
                write_msg(item[u'user_id'],u'Wow, dude, look what you found! Spinner like you wanted - plastic and for 5 euros. Wait, but the color? Type black, blue or white.')
            elif response['items'][0]['body'] == 'blue':
                write_msg(item[u'user_id'],u'Fuh, it was not easy, but I found it. Blue plastic spinner for 5 euros. Come to our site and buy it. Right now. JUST DO IT! http://spinn.ee/toode/spinner-1/')
            elif response['items'][0]['body'] == 'black':
                write_msg(item[u'user_id'],u'Fuh, it was not easy, but I found it. Black plastic spinner for 5 euros. Come to our site and buy it. Right now. JUST DO IT! http://spinn.ee/toode/spinner-1/')
            elif response['items'][0]['body'] == 'white':
                write_msg(item[u'user_id'],u'Fuh, it was not easy, but I found it. White plastic spinner for 5 euros. Come to our site and buy it. Right now. JUST DO IT! http://spinn.ee/toode/spinner-1/')
            else:
                write_msg(item[u'user_id'],u'Sorry, I dont understand you. Try ask again')
        time.sleep(1)