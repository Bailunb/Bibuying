from django.shortcuts import render
import json
from BibuyingIndex import Trynm as music_idx
import os
from BibuyingData.CharRNN.sample import write_song as get_song


def all_templates(request):
	return render(request, 'index.html')


def index(request):
	category = ({'idx': 0, 'name': '民族'},
	            {'idx': 1, 'name': '年代港乐'},
	            {'idx': 2, 'name': '未出名'},
	            {'idx': 3, 'name': '年轻一代'},
	            {'idx': 4, 'name': '音乐节'},
	            {'idx': 5, 'name': '民谣'},
	            {'idx': 6, 'name': '朗朗上口'},
	            {'idx': 7, 'name': '年轻港乐'},
	            {'idx': 8, 'name': '最热门'},
	            {'idx': 9, 'name': '卖萌'},)
	# for word cloud
	artists_path = os.getcwd() + '/ArtistsData/'
	singers = []
	for f in os.listdir(artists_path):
		f = os.path.splitext(f)
		if f[1] == ".txt":
			singers.append(f[0])
	return render(request, 'home.html', locals())


def search_result(request):
	words = request.GET['words']
	print(words)
	# error here

	music_idx.query(words)  # this operation edit 'search_result.txt'
	songs = open('BibuyingWeb/static/search_result.txt', encoding='utf-8').read().split()
	music = []
	for song in songs:
		file_name = 'SongsData/%s.json' % str(song)
		# print(file_name)
		info = json.load(open(file_name, 'r', encoding='utf-8'))
		info['song_lyric'] = info['song_lyric'][:100] + '...'
		info['detail_url'] = "/details/?song_id=%s" % song
		music.append(info)

	return render(request, 'search_result.html', locals())


def details(request):
	song_id = request.GET['song_id']
	info = json.load(open('SongsData/%s.json' % str(song_id), 'r', encoding='utf-8'))
	song_lyric = info['song_lyric'].split('\n')
	play_src = "//music.163.com/outchain/player?type=2&id=%s&auto=0&height=66" % song_id
	return render(request, 'details.html', locals())


def worldcloud(request):
	singer = request.GET['singer']
	pic1 = 'images/artists/%s.jpg' % singer
	pic0 = 'images/artists/%s0.jpg' % singer
	return render(request, 'wordcloud.html', locals())


def write_song(request):
	word = request.GET['words']
	if word == '': word = u'无题'
	catalog = request.GET['demo-category']
	script = get_song(catalog, word, 'BibuyingData/CharRNN/')
	# print(script)
	return render(request, 'write.html', locals())
