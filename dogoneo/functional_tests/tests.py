from django.test import LiveServerTestCase
from shelter.models import Dog
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(ChromeDriverManager().install())	

	def tearDown(self):
		self.browser.quit()

	def test_can_get_home_page(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Dogoneo', self.browser.title)



if __name__ == '__main__':
	unittest.main()
