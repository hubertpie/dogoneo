from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(ChromeDriverManager().install())	

	def tearDown(self):
		self.browser.quit()

	def test_can_get_home_page(self):
		#he is trying to open a new page that has dogs from different shelters in one place
		self.browser.get('http://localhost:8000')

		#noticed the page header - dogoneo
		self.assertIn('Dogoneo', self.browser.title)

		#at the home page he noticed list of dogs with their name and basic data
		dog_list = self.browser.find_element_by_tag_name('ul').text
		self.assertIn('Zbyszek', dog_list)
		#also noted a feature to filter results based on size, age, town
		search_form = self.browser.find_element_by_tag_name('form')
		self.assertIn('Search', search_form)
		self.fail('Done')



if __name__ == '__main__':
	unittest.main()
