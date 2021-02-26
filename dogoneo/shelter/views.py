from django.shortcuts import render
from shelter.models import Dog

def home_page(request):
	dogs = Dog.objects.all()
	return render(request, 'home_page.html', {'dogs': dogs})