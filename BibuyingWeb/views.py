from django.shortcuts import render
import json


def index(request):
	return render(request, 'home.html')


def search_result(request):
	words = request.GET['words']
	print('words = ', words)
	# add queries here
	# : music_idx.query(words) # this operation edit 'search_result.txt'

	songs = open('BibuyingWeb/static/search_result.txt').read().split()
	music = []
	for song in songs:
		file_name = 'SongsData/%s.json' % str(song)
		info = json.load(open(file_name, 'rb'))
		info['song_lyric'] = info['song_lyric'][:100] + '...'
		info['detail_url'] = "/details/?song_id=%s" % song
		music.append(info)
	return render(request, 'search_result.html', locals())


def details(request):
	song_id = request.GET['song_id']
	info = json.load(open('SongsData/%s.json' % str(song_id), 'rb'))
	song_lyric = info['song_lyric'].split('\n')
	play_src = "//music.163.com/outchain/player?type=2&id=%s&auto=0&height=66" % song_id
	return render(request, 'details.html', locals())
