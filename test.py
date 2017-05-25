# -*- coding: utf-8 -*-
# Code for testing VK chat bot.

import unittest
from vkbot import check

class Test(unittest.TestCase):
    def test_value(self):
        response = "Hi man! Do you want to buy a spinner? If yes, type 1."
        answer = check("Hi")
        print (answer)
        self.assertEqual(answer, response)



if __name__ == '__main__':
    unittest.main()
