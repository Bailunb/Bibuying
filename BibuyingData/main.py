import json
import requests
import jieba
import os.path
from bs4 import BeautifulSoup
import re
import get_ips

ips = [
	'222.95.37.169:48785'
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36', "Authorization": get_ips.auth}


def get_soup(web_url):
	# html_file = open("web.html", "w", encoding='utf-8')
	if not 'lyric' in web_url: print(web_url)
	proxy = {"http": "http://" + ips[0], "https": "https://" + ips[0]}
	
	req = requests.get(url=web_url, headers=headers, proxies=proxy)
	soup = BeautifulSoup(req.text, 'lxml')
	# html_file.write(soup.prettify())
	return soup


def init_artist_id():
	ids_file = open('artist_id.txt', 'w', encoding='utf-8')
	for i in range(1, 4):
		discover_url = 'http://music.163.com/discover/artist/cat?id=100%d' % i
		soup = get_soup(discover_url)
		ids = soup.find_all('a', attrs={"class": "nm nm-icn f-thide s-fc0"})
		pattern = re.compile(r'id=\d+')
		for id in ids:
			st = pattern.findall(str(id))
			ids_file.write(st[0][3:] + '\n')
			

def get_artists():
	file = open('artist_id.txt', 'r')
	ans = []
	for line in file:
		ans.append(int(line))
	return ans
	
	# ------------------------------------------------------------------------------------


def get_lyric(song_id):
	lyric_url = 'http://music.163.com/api/song/lyric?id=%s&lv=1&kv=1&tv=-1' % str(song_id)
	lyric = get_soup(lyric_url).text
	try:
		j = json.loads(lyric)
		try:
			lrc = j['lrc']['lyric']
			pat = re.compile(r'\[.*\]')
			return re.sub(pat, "", lrc).strip()
		except KeyError:
			return ""
	except json.decoder.JSONDecodeError:
		return ''


def get_pic(song_id):
	song_url = 'http://music.163.com/song?id=%s' % str(song_id)
	soup = get_soup(song_url)
	st = soup.find('script', attrs={"type": "application/ld+json"}).text
	pat = re.compile(r'\"images\": \[.*\]')
	return pat.findall(st)[0][12:-2]


def get_words(lyric):
	word_lst = []
	seg_list = jieba.cut(lyric, cut_all=True)
	for word in seg_list:
		if word != '' and not '\n' in word:
			word_lst.append(word)
	return word_lst


def construct_song(artist_name, song_id, song_name):
	ans = {}
	ans["artist_name"] = artist_name
	ans["song_name"] = song_name
	ans['song_id'] = song_id
	ans['song_lyric'] = get_lyric(song_id)
	ans['pic_url'] = get_pic(song_id)
	ans['words'] = get_words(ans['song_lyric'])
	
	path = os.path.dirname(os.getcwd()) + '\\SongsData\\'
	json_str = repr(ans).replace('\'', '\"').replace(',', ',\n')
	file_name = '%s.json' % str(song_id)
	with open(path + file_name, 'w', encoding='utf-8') as w:
		w.write(json_str)
		

def append_50music(artist_id):
	list_url = 'http://music.163.com/artist?id=%d' % artist_id
	soup = get_soup(list_url)
	
	artist_name = soup.find('h2').text
	print(artist_name)
	
	song_list = soup.find('ul', attrs={"class": "f-hide"})
	song_list = song_list.find_all('a')
	
	pattern = re.compile(r'id=\d+')
	for song in song_list:
		song_name = song.text
		song_id = pattern.findall(str(song))[0][3:]
		print(song_name, song_id)
		construct_song(artist_name, song_id, song_name)


def main():
	# init_artist_id()
	artists = get_artists()
	for i in range(297, 301):
		print('i = %d' % i, end=' ')
		append_50music(artists[i])
	

if __name__ == '__main__':
	main()
	# print(get_lyric(360941))
