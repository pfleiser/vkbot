SPINNBOT
========

Chat bot for VK social network

## Installations

0. Make your page on VK and open 'Manage community'.
1. Install module vk_api: `pip install vk_api`
2. Don't forget to edit vkbot.py. There you should enter your token access (you can find it in Manage community --> API usage tab). If you're a person, not a page, add this line instead of token:
#vk = vk_api.VKApi(login='login', password='123456')
4. Run! `python vkbot.py`

## Idea

Chat bot helps users to communicate with new web-shop which sels fidget spinners.
Current situation - basic template answers with options. In the future - straight connection of chat bot to web-shop backet and direct order.

## Licence

This code uses GNU licence. Peace :)
