import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver=webdriver.Chrome(executable_path="E:\Work Files\Webdrives_for_Automation\chromedriver.exe")
        driver.get("https://www.google.com/")
        self.assertTrue(driver.title=="Google")
        #self.assertFalse(driver.title == "Google")

        #driver=None
        #self.assertIsNone(driver)
        self.assertLess(10,12)  #first value compares with second value, so,10<12 it's true

        List=("python","java")
        self.assertIn("python",List)

if __name__=="__main__":
    unittest.main()

