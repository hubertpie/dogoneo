from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from shelter.views import home_page
from shelter.models import Dog
from datetime import datetime

class HomePageTest(TestCase):

	def test_root_url_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_return_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected = render_to_string('home_page.html')
		self.assertEqual(response.content.decode(), expected)


class DogModelTest(TestCase):

	def test_adding_and_retrieving_dog(self):

		test_dog = Dog()
		test_dog.name = 'Zbyszek'
		test_dog.short_description = 'Uczy się chodzić na smyczy'
		test_dog.gender = 'male'
		test_dog.age = 10
		test_dog.accepts_cat = 'Nie sprawdzono'
		test_dog.accepts_dogs = 'Nie sprawdzono'
		test_dog.is_sterilised = True
		test_dog.is_castrated = True
		test_dog.is_vaccinated = True
		test_dog.has_chip = True
		test_dog.save()

		# TODO: change way of testing models
		dogs = Dog.objects.all()
		self.assertEqual(dogs[0].name, 'Zbyszek')
		self.assertEqual(dogs[0].short_description, 'Uczy się chodzić na smyczy')
		self.assertEqual(dogs[0].gender, 'male')
		self.assertEqual(dogs[0].age, 10)
		self.assertEqual(dogs[0].accepts_cat, 'Nie sprawdzono')
		self.assertEqual(dogs[0].accepts_dogs, 'Nie sprawdzono')
		self.assertEqual(dogs[0].is_sterilised, True)
		self.assertEqual(dogs[0].is_castrated, True)
		self.assertEqual(dogs[0].is_vaccinated, True)
		self.assertEqual(dogs[0].has_chip, True)