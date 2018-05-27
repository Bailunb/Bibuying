import os
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import jieba

d = path.dirname(__file__)


def get_word_cloud(path_name, file_name):
    # get text && get fonts & mask_image
    text = open(path_name + file_name + '.txt', "r", encoding='utf-8').read()
    text = ' '.join(jieba.cut(text, cut_all=True))
    font = os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")
    coloring = np.array(Image.open(path.join(d, path_name + file_name + '.jpg')))
    # coloring = np.array(Image.open(path.join(d, 'bg.png')))
    # set stopwords
    stopwords = set(STOPWORDS)
    ignore_words = ['作曲', '作词', '制作', '作人', '乐队', '录音', '录音室', '录音师',
                    '工作', '工作室', '编曲', 'Studio', '混音']
    ignore_words.append(file_name)
    for item in ignore_words:
        stopwords.add(item)

    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white", font_path=font, stopwords=stopwords,
                          mask=coloring, random_state=2, margin=1).generate(text)
    wordcloud = wordcloud.recolor(color_func=ImageColorGenerator(coloring))

    # Display the generated image, the matplotlib way:
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    plt.savefig(path_name + file_name + '0.jpg')
    plt.show()
    plt.close()


def main():
    artists_path = os.path.dirname(os.path.dirname(os.getcwd())) + '/ArtistsData/'
    files = os.listdir(artists_path)

    cnt = 0
    for f in files:
        f = os.path.splitext(f)
        if f[1] == ".txt":
            cnt += 1
            # if cnt > 1: break
            print('%s (%d/%d)' % (f, cnt, 302 ))
            get_word_cloud(artists_path, f[0])
    print('word_cloud, done')


if __name__ == "__main__":
    # artists_path = os.path.dirname(os.path.dirname(os.getcwd())) + '/ArtistsData/'
    # get_word_cloud(artists_path, 'dan.txt')
    # main()
    artists_path = os.path.dirname(os.path.dirname(os.getcwd())) + '/ArtistsData/'
    get_word_cloud(artists_path, '周杰伦')
    pass
