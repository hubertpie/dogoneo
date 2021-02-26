from django.db import models


class Dog(models.Model):
	GENDER_CHOICE = (
		('male', 'Samiec'),
		('female', 'Samica'))

	name = models.CharField(max_length=100, db_index=True)
	short_description = models.TextField(blank=True)
	gender = models.CharField(max_length=7, choices=GENDER_CHOICE)
	age = models.IntegerField()
	accepts_cat = models.TextField(blank=True)
	accepts_dogs = models.TextField(blank=True)
	is_sterilised = models.BooleanField(default=False)
	is_castrated = models.BooleanField(default=False)
	is_vaccinated = models.BooleanField(default=False)
	has_chip = models.BooleanField(default=False)
