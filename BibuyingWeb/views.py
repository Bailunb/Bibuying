from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import json


def index(request):
	return render(request, 'home.html')


def search_result(request):
	
	return render(request, 'search_result.html')


def details(request):
	info = json.load(open('BibuyingWeb/test.json', 'rb'))
	song_id = info['song_id']
	song_name = info['song_name']
	song_lyric = info['song_lyric']
	pic_url = info['pic_url']
	play_src = "//music.163.com/outchain/player?type=2&id=%s&auto=1&height=66" % song_id
	# print(song_lyric)
	return render(request, 'details.html', locals())
