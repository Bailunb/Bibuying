import os
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from bs4 import BeautifulSoup
import requests
from BibuyingData.main import get_artists

d = path.dirname(__file__)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) ''AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/51.0.2704.63 Safari/537.36'}


def getWordCloud():
    # get text && get fonts & maskimage
    text = open("dan.txt", "r", encoding='utf-8').read()
    font = os.path.join(os.path.dirname(__file__), "../word_cloud/DroidSansFallbackFull.ttf")
    coloring = np.array(Image.open(path.join(d, "../word_cloud/bg.png")))
    
    # set stopwords
    stopwords = set(STOPWORDS)
    ignorewords = ['蚊子的蚊子', '伟大的蚊子', '乔丹', '图片', '您好', '我现在有事不在',
                   '一会再和您联系', '系统消息', '你撤回了一条消息','GLOW', '动作消息','表情',
                   '陈秋雨','google','https','maps','我在这里','点击查看',
                   '对方已成功接收了您发送的离线文件','zh','CN','曹艺舰','海鱼','culex',
                   'Believe','放手会冷','曹艺舰给您发送了一个窗口抖动','html',
                   '蚊子的蚊子给您发送了一个窗口抖动']
    for item in ignorewords:
        stopwords.add(item)
    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white",font_path=font,stopwords=stopwords,
                          mask=coloring, random_state=2,margin=1).generate(text)
    wordcloud = wordcloud.recolor(color_func=ImageColorGenerator(coloring))
    # Display the generated image, the matplotlib way:
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    plt.savefig("jordan2.png")
    plt.show()
    plt.close()


def get_soup(web_url):
    html_file = open("web.html", "w", encoding='utf-8')
    req = requests.get(url=web_url, headers=headers)
    soup = BeautifulSoup(req.text, features='lxml')
    # html_file.write(soup.prettify())
    return soup


def get_artist_name():
    artists_id = get_artists()
    artists = []
    for cur_id in artists_id:
        soup = get_soup('http://music.163.com/artist?id=' + str(cur_id))
        artists.append({'id': cur_id,
                        'name': soup.find('h2', attrs={'class': 'sname f-thide sname-max'}).string,
                        'description': soup.find(attrs={"name": "description"})['content']})
        print(artists[-1])
    print(artists)


if __name__ == "__main__":
    getWordCloud()
