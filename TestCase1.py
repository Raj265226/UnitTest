import unittest

def setUpModule():   #will be executed before executing any class
    print("setupModule")

def tearDownModule():  #After completing everything
    print("teardownModule")


class Apptesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")

    @classmethod
    def setUpClass(cls):
        print("Open Application")

    @classmethod
    def tearDownClass(cls):
        print("Close Application")

    def test_search(self):
        print("This is search test")

    @unittest.skip("test")
    def test_advancesearch(self):
        print("This is advance search test")

    @unittest.SkipTest
    def test_prepaidrecharge(self):
        print("This is prepaid recharge")

    def test_postpaidrecharge(self):
        print("This is postpaid recharge")

if __name__=="__main__":
    unittest.main()
