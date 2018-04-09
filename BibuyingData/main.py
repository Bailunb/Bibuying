# -*- coding:utf-8 -*-
import json
import urllib.request
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import csv
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}


def get_soup(web_url):
	html_file = open("web.html", "w", encoding='utf-8')
	print(web_url)
	
	req = urllib.request.Request(url=web_url, headers=headers)
	# print(req)
	web_page = urllib.request.urlopen(req)
	data = web_page.read()
	soup = BeautifulSoup(data, 'lxml')
	html_file.write(soup.prettify())
	return soup


def play_json():
	data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
	data = json.dumps(data)
	print(data)


def get_artist_id():
	ids_file = open('artist_id.txt', 'w', encoding='utf-8')
	for i in range(1, 4):
		discover_url = 'http://music.163.com/discover/artist/cat?id=100%d' % i
		soup = get_soup(discover_url)
		ids = soup.find_all('a', attrs={"class": "nm nm-icn f-thide s-fc0"})
		pattern = re.compile(r'id=\d+')
		for id in ids:
			st = pattern.findall(str(id))
			ids_file.write(st[0][3:] + '\n')
			# print(st[0][3:])
		# print(len(ids))


def append_music_list(artist_id):
	list_url = 'http://music.163.com/artist?id=6452'
	
	soup = get_soup(list_url)
	


def main():
	# get_artist_id()
	append_music_list(6452)
	

if __name__ == '__main__':
	main()
