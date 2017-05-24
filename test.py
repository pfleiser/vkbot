# -*- coding: utf-8 -*-
# Code for testing VK chat bot.

import unittest
from vkbot import check

class Test(unittest.TestCase):
    def test_value(self):
        response = "Hi"
        answer = check(response)
        self.assertEqual("Hi man! Do you want to buy a spinner? If yes, type 1.", answer)



if __name__ == '__main__':
    unittest.main()