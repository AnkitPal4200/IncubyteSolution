import unittest
from Test1 import Test1
from unittest.mock import patch
from Logger import Logger

class MyTestCase(unittest.TestCase):

    def test_leap_year400(self):
        t=Test1()
        result=t.leap_year(400)

        self.assertEqual(result, True)

    def test_leap_year1700(self):
        t=Test1()
        result=t.leap_year(1700)

        self.assertEqual(result, False)# add assertion here

    def test_leap_year2008(self):
        t=Test1()
        result=t.leap_year(2008)

        self.assertEqual(result, True)

    def test_leap_year2007(self):
        t=Test1()
        result=t.leap_year(2019)

        self.assertEqual(result, False)


    def test_invocation(self):
        with patch.object(Logger,"log") as mock:
            obj=Test1()
            obj.leap_year(2008)













if __name__ == '__main__':
    unittest.main()
