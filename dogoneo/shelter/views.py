from django.shortcuts import render, get_object_or_404
from shelter.models import Dog

def dog_list(request):
	dogs = Dog.objects.all()
	return render(request, 'shelter/list.html', {'dogs': dogs})

def dog_detail(request, id):
	dog = get_object_or_404(Dog, id=id)
	return render(request, 'shelter/detail.html', {'dog': dog})