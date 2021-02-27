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
		#he is trying to open a new page that has dogs from different shelters in one place
		self.browser.get(self.live_server_url)

		#noticed the page header - dogoneo
		self.assertIn('Dogoneo', self.browser.title)

		#at the home page he noticed list of dogs with their name and basic data
		dog_list = self.browser.find_element_by_tag_name('ul')
		self.assertTrue(dog_list)
		#also noted a feature to filter results based on size, age, town
		search_form = self.browser.find_element_by_tag_name('form')
		search_button = self.browser.find_element_by_tag_name('input').get_attribute("value")
		self.assertTrue(search_form)
		self.assertEqual('Search', search_button)
		self.fail('Done')



if __name__ == '__main__':
	unittest.main()
