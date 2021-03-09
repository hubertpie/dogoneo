from django.db import models
from django.urls import reverse

class Dog(models.Model):
	GENDER_CHOICE = (
		('male', 'Samiec'),
		('female', 'Samica'))

	name = models.CharField(max_length=100, db_index=True)
	short_description = models.TextField(blank=True)
	gender = models.CharField(max_length=7, choices=GENDER_CHOICE)
	age = models.CharField(max_length=30)
	image = models.ImageField(upload_to='dogs/%Y/%m/%d', blank=True)
	weight = models.CharField(max_length=10)
	accepts_adults = models.TextField(blank=True)
	accepts_kids = models.TextField(blank=True)
	accepts_cats = models.TextField(blank=True)
	accepts_dogs = models.TextField(blank=True)
	is_sterilised = models.TextField(blank=True)
	is_vaccinated = models.TextField(blank=True)
	has_chip = models.TextField(blank=True)

	class Meta:
		ordering = ('name', )

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('dog_detail', args=[self.id])