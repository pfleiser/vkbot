# -*- coding: utf-8 -*-
# Code for testing VK chat bot.

import unittest
from vkbot import start

class Test(unittest.TestCase):
    def test_value(self):
        result = start()
        self.assertEqual("Hi man! Do you want to buy a spinner? If yes, type 1.", result)



if __name__ == '__main__':
    unittest.main()