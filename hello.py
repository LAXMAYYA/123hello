import unittest
from selenium import webdriver

class WebsiteLoadingTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver (assuming you have installed and configured it properly)
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()

    def test_website_loading(self):
        # Open the atg.world website
        self.driver.get("https://www.atg.world")

        # Verify that the website has loaded successfully
        page_title = self.driver.title
        self.assertEqual(page_title, "atg.world")

if __name__ == "__main__":
    unittest.main()
