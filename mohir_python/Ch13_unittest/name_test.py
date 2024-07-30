# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:31:08 2024

@author: Elyorbek
"""

# testing the get_name function

import unittest
from name import get_name

class NameTest(unittest.TestCase):
    def test_get_name(self):
        name = get_name("diyor", "aliyev")
        self.assertEqual(name, "Diyor Aliyev")

unittest.main()
    