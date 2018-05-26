import os
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from bs4 import BeautifulSoup
import requests
from BibuyingData.main import get_artists
from io import BytesIO
import jieba
import json

d = path.dirname(__file__)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) ''AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}


def getWordCloud():
    # get text && get fonts & mask_image
    text = open("dan.txt", "r", encoding='utf-8').read()
    text = ' '.join(jieba.cut(text, cut_all=True))
    font = os.path.join(os.path.dirname(__file__), "../word_cloud/DroidSansFallbackFull.ttf")
    coloring = np.array(Image.open(path.join(d, "../word_cloud/bg.png")))
    
    # set stopwords
    stopwords = set(STOPWORDS)
    ignore_words = ['哈', '哈哈', '哈哈哈', '哈哈哈哈','伟大', '蚊子', '乔丹', '图片', '您好',
                    '我现在有事不在',
                   '一会再和您联系', '系统消息', '你撤回了一条消息','GLOW', '动作消息','表情',
                   '陈秋雨','google','https','maps','我在这里','点击查看',
                   '对方已成功接收了您发送的离线文件','zh','CN','曹艺舰','海鱼','culex',
                   'Believe','放手会冷','曹艺舰给您发送了一个窗口抖动','html',
                   '蚊子的蚊子给您发送了一个窗口抖动']
    for item in ignore_words:
        stopwords.add(item)
    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white", font_path=font, stopwords=stopwords,
                          mask=coloring, random_state=2, margin=1).generate(text)
    wordcloud = wordcloud.recolor(color_func=ImageColorGenerator(coloring))
    # Display the generated image, the matplotlib way:
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    plt.savefig("jordan2.png")
    # plt.show()
    plt.close()


def get_soup(web_url):
    html_file = open("web.html", "w", encoding='utf-8')
    req = requests.get(url=web_url, headers=headers)
    soup = BeautifulSoup(req.text, features='lxml')
    # html_file.write(soup.prettify())
    return soup


def get_artist_info(cur_id: int, path_name: str):
    soup = get_soup('http://music.163.com/artist?id=' + str(cur_id))
    artist_name = soup.find('h2', attrs={'class': 'sname f-thide sname-max'}).string

    # save image for each artist
    img = requests.get(soup.find('div', attrs={'class': 'n-artist f-cb'}).img['src'])
    image = Image.open(BytesIO(img.content))
    image.save('%s%s.jpg' % (path_name, artist_name))

    # save description for the artist
    txt_file = open('%s%s.txt' % (path_name, artist_name), 'w', encoding='utf-8')
    txt_file.write(soup.find(attrs={"name": "description"})['content'])

    print(artist_name)


def get_artists_info():
    artists_id = get_artists()
    path_name = os.path.dirname(os.getcwd()) + '/ArtistsData/'
    cnt = 0
    for cur_id in artists_id:
        get_artist_info(cur_id, path_name)
        print('cnt = ' + str(cnt))
        cnt += 1
    print('done')


def give_songs_to_artists():
    songs_path = os.path.dirname(os.getcwd()) + '/SongsData/'
    artists_path = os.path.dirname(os.getcwd()) + '/ArtistsData/'
    song_files = os.listdir(songs_path)
    for i in range(len(song_files)):
        if song_files[i] == 'fuck.py': continue
        with open("%s%s" % (songs_path, song_files[i]), encoding='utf-8') as f:
            song = json.load(f)
            txt = []
            with open('%s%s.txt' % (artists_path, song['artist_name']),encoding='utf-8') as f_to:
                txt += f_to.readlines()
                txt.append('\n')
                txt.append(song['song_lyric'])
            with open('%s%s.txt' % (artists_path, song['artist_name']), 'w', encoding='utf-8') as f_to:
                print(txt)
                f_to.writelines(txt)
        # print(song['song_lyric'])


if __name__ == "__main__":
    # get_artists_info()
    give_songs_to_artists()
    # getWordCloud()
    pass
