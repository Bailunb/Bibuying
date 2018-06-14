from django.shortcuts import render
import json
from BibuyingIndex import main as music_idx
import os


def all_templates(request):
	return render(request, 'index.html')


def index(request):
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
		print(file_name)
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
