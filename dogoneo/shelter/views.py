from django.shortcuts import render
from shelter.models import Dog

def dog_list(request):
	dogs = Dog.objects.all()
	return render(request, 'shelter/list.html', {'dogs': dogs})