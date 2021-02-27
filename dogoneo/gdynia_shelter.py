import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dogoneo.settings')
django.setup()

from django.core.files.base import ContentFile
from shelter.models import Dog
from bs4 import BeautifulSoup
import requests
import urllib.request
import re

re_delete_special_char = '[\n\t/]+'
ciapkowo_main_dog_page = 'http://ciapkowo.pl/filter/psy/'
result = requests.get(ciapkowo_main_dog_page)


def find_all_dogos_on_page(soup):
	dogos = soup.find_all('div', {'class': 'card h-100'})
	dogs = [requests.get(dog.find_all('a', href=True)[0]['href']) for dog in dogos]
	return [dog for dog in dogs if dog.status_code == 200]

def insert_into_db(dogo_page):
	dogo_soup = BeautifulSoup(dogo_page.content, 'html.parser')
	dogo_info = dogo_soup.find('ul', {'class': 'list-group list-group-flush'})

	dogo_information = {}

	for info in dogo_info.find_all('li', {'class': 'list-group-item d-flex justify-content-between'}):
		info_content = info.find_all('div')
		try:
			label = re.sub(re_delete_special_char, '', str(info_content[0].contents[0]))
			if 'span' in str(info_content):
				value = info_content[1].find('span')['title']
			else:
				value = re.sub(re_delete_special_char, '', str(info_content[1].contents[0]))
		except Exception:
			value = 'Brak informacji'
		dogo_information[label] = value
	dogo_img_div = dogo_soup.find('div', {'class': 'col mb-3'})
	dogo_name = re.sub(re_delete_special_char, '', dogo_soup.find('h1', {'class': 'js-name'}).contents[0])
	dogo_img_src = dogo_img_div.find('img')['src']

	dog = Dog(name=dogo_name,
				  gender=dogo_information['Płeć'],
				  short_description=dogo_information.get('Dla kogo?', 'Brak informacji'),
				  age=dogo_information.get('Wiek', 'Brak informacji'),
				  accepts_adults=dogo_information.get('Stosunek do dorosłych', 'Brak informacji'),
				  accepts_kids=dogo_information.get('Stosunek do dzieci', 'Brak informacji'),
				  accepts_cats=dogo_information.get('Stosunek do kotów', 'Brak informacji'),
				  accepts_dogs=dogo_information.get('Stosunek do psów', 'Brak informacji'),
				  has_chip=dogo_information.get('Czip', 'Brak informacji'),
				  is_sterilised=dogo_information.get('Kastracja  sterylizacja', 'Brak informacji'),
				  is_vaccinated=dogo_information.get('Szczepienie  odrobaczenie  odpchlenie', 'Brak informacji'),
				  )
	img_request=requests.get(dogo_img_src)
	if img_request.status_code == 200:
		dog.image.save(dogo_name, ContentFile(img_request.content), save=True)


if __name__=='__main__':
	if result.status_code == 200:
		first_page = BeautifulSoup(result.content, 'html.parser')
		pages = first_page.find_all('li', {'class': 'page-item'})
		max_page = max([int(x) for x in re.findall("\d+", str(pages))])

		for x in range(max_page):
			result = requests.get(ciapkowo_main_dog_page + '/page/' + str(x+1))
			if result.status_code == 200:
				page = BeautifulSoup(result.content, 'html.parser')
				dogs = find_all_dogos_on_page(page)
				for dog in dogs:
					insert_into_db(dog)

