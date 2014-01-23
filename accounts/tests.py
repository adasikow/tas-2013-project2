from selenium import webdriver
from django.test import LiveServerTestCase

class LoginTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get(self.live_server_url + '/products/')
        title = self.browser.title
        self.assertIn('', title)
