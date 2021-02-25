from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from shelter.views import home_page

class HomePageTest(TestCase):

	def test_root_url_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_return_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected = render_to_string('home_page.html')
		self.assertEqual(response.content.decode(), expected)