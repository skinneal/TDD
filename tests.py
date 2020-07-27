# Title: tests.py (A2)
# Author: Allison Skinner
# Date: 7/27/2020

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    # Empty String
    def test_1(self):
        pwd = ''
        self.assertFalse(check_pwd(pwd))

    # 7 characters < 8
    def test_2(self):
        pwd = 'pA5$wrd'
        self.assertFalse(check_pwd(pwd))       

if __name__ == '__main__':
    unittest.main()
