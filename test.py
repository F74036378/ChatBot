import requests
import re
from bs4 import BeautifulSoup

r = requests.get('http://www.atmovies.com.tw/showtime/t06602/a06/')

content = r.content
soup = BeautifulSoup(content, 'html.parser')

for ul in soup.findAll('ul', id='theaterShowtimeTable'):
	for a in ul.find_all('a', href=re.compile('^/movie/')):
		print(a.text)
	for ul1 in ul.findAll('li', text=re.compile('\d{1,2}\S\S\d{1,2}')):
		print(ul1.text)