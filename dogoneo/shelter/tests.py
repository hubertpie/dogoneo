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

	def test_home_page_display_all_dogs(self):
		test_dog = Dog()
		test_dog.name = 'Zbyszek'
		test_dog.gender = 'male'
		test_dog.age = 10
		test_dog.save()
		test_dog2 = Dog()
		test_dog2.name = 'Zbyszkowa'
		test_dog2.gender = 'female'
		test_dog2.age = 6
		test_dog2.save()

		request = HttpRequest()
		response = home_page(request)

		self.assertIn('Zbyszek', response.content.decode())
		self.assertIn('Zbyszkowa', response.content.decode())

class DogModelTest(TestCase):

	def test_adding_and_retrieving_dog(self):

		test_dog = Dog()
		test_dog.name = 'Zbyszek'
		test_dog.short_description = 'Uczy się chodzić na smyczy'
		test_dog.gender = 'male'
		test_dog.age = 10
		test_dog.save()

		# TODO: change way of testing models
		dogs = Dog.objects.all()
		self.assertEqual(dogs[0].name, 'Zbyszek')
		self.assertEqual(dogs[0].short_description, 'Uczy się chodzić na smyczy')
		self.assertEqual(dogs[0].gender, 'male')
		self.assertEqual(dogs[0].age, 10)

	def test_creating_dog_with_funny_gender(self):

		test_dog = Dog()
		test_dog.name = 'Zbyszek'
		test_dog.short_description = 'Uczy się chodzić na smyczy'
		test_dog.gender = 'male'
		test_dog.age = 10
		test_dog.save()

		# TODO: change way of testing models
		dogs = Dog.objects.all()
		self.assertEqual(dogs[0].name, 'Zbyszek')
		self.assertEqual(dogs[0].short_description, 'Uczy się chodzić na smyczy')
		self.assertEqual(dogs[0].gender, 'male')
		self.assertEqual(dogs[0].age, 10)