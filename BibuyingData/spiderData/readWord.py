import json
import jieba
import os.path
# import  requests
from bs4 import BeautifulSoup
from sklearn import metrics, cluster
from sklearn.feature_extraction.text import  CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD

def read_from_file(file_name):
    with open(file_name,"r",encoding='UTF-8') as fp:
        words = fp.read()
    return words

def readContent():
    f1 = open('after.txt', 'w',encoding='UTF-8')
    # path = "./ArtistsData" #文件夹目录
    path = "../../ArtistsData"  #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    s = []
    for file in files: #遍历文件夹
         if not os.path.isdir(file) and os.path.splitext(file)[1] == '.txt': #判断是否是文件夹，不是文件夹才打开
              f = open(path+"/"+file,encoding='UTF-8'); #打开文件
              iter_f = iter(f); #创建迭代器
              str = ""
              for line in iter_f: #遍历文件，一行行遍历，读取文本
                  str = str + line
              s.append(str) #每个文件的文本存到list中
    print(s,file=f1)
    # print(s) #打印结果
    f1.close()
    return s

def jiebaCut(s,new_stopwords):
    f2 = open('word_lst.txt', 'w', encoding='UTF-8')
    word_lst = []
    for s1 in s:
        seg_list=jieba.lcut(s1,cut_all=True)
        new_s1Words=del_stop_words(seg_list,new_stopwords)
        word_lst.append(' '.join(new_s1Words))
    print(word_lst,file=f2)
    f2.close()
    return  word_lst


def stop_words(stop_word_file):
    words = read_from_file(stop_word_file)
    result = jieba.cut(words)
    new_stopwords = []
    for r in result:
        new_stopwords.append(r)
    return set(new_stopwords)

def del_stop_words(seg_list,stop_words_set):
#   seg_list是已经切词但是没有去除停用词的文档。
#   返回的会是去除停用词后的文档
    new_words = []
    for r in seg_list:
        if r not in stop_words_set and r!='' and '\n' not in r:
            new_words.append(r)
    return new_words

def lyricsBlending():
    path = "../../ArtistsData"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    # f6 = open('kmeans_labels.txt', 'w', encoding='UTF-8')
    words=read_from_file('kmeans_labels.txt')
    count=0
    for i in words:
        if i=='[' or i==']' or i==','or i=='\n':
            continue
        count=count+1
        count1=0
        i0=int(i)
        f7 = open('%d.txt'%(i0), 'a+', encoding='UTF-8')

        for file in files:  # 遍历文件夹
            if not os.path.isdir(file) and os.path.splitext(file)[1] == '.txt':  # 判断是否是文件夹，不是文件夹才打开
                count1=count1+1
                if count1==count:
                    content1=read_from_file(path+"/"+file)
                    print(content1,file=f7)
                    break
        f7.close()


def delblankline():
    path = "../CharRNN/data"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    count=0
    for file in files:  # 遍历文件夹
        f8 = open(path+'/%d_New.txt' % (count), 'a+', encoding='UTF-8')
        infopen = open(path+"/"+file, 'r',encoding='UTF-8')
        lines = infopen.readlines()
        for line in lines:
            if line.split():
                f8.writelines(line)
            else:
                f8.writelines("")
        infopen.close()
        f8.close()
        count=count+1

def categorySinger():
    path = "../../ArtistsData"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    # f6 = open('kmeans_labels.txt', 'w', encoding='UTF-8')
    words=read_from_file('kmeans_labels.txt')
    count=0
    for i in words:
        if i=='[' or i==']' or i==','or i=='\n':
            continue
        count=count+1
        count1=0
        i0=int(i)
        f9 = open('%d_singer.txt'%(i0), 'a+', encoding='UTF-8')

        for file in files:  # 遍历文件夹
            if not os.path.isdir(file) and os.path.splitext(file)[1] == '.txt':  # 判断是否是文件夹，不是文件夹才打开
                count1=count1+1
                if count1==count:
                    content1=os.path.splitext(file)[0]
                    print(content1,file=f9)
                    break
        f9.close()

if __name__ == '__main__':
    # lyricsBlending()
    # delblankline()
    categorySinger()



#     f3=open('kmeans_labels.txt', 'w', encoding='UTF-8')
#     f4 = open('retfidf.txt', 'w', encoding='UTF-8')
#     f5 = open('freqMatrix.txt', 'w', encoding='UTF-8')
#     s=readContent()
#     new_stopwords=stop_words('stopwords.txt')
#     word_lst=jiebaCut(s,new_stopwords)
#
# # 到这里 文档的分词和去除停用词结束
#     print("文档的分词和去除停用词结束")
#
# #开始建立tf-idf矩阵
#
#
#     vectorizer = CountVectorizer()
#     transformer = TfidfTransformer()
#     #得到词频矩阵
#     freqMatrix=vectorizer.fit_transform(word_lst)
#     print("得到词频矩阵",freqMatrix.shape)
#     print(freqMatrix,file=f5)
#
#     #pca降维
#     PCAfreqMatrix = TruncatedSVD(n_components=100).fit_transform(freqMatrix)
#     print("pca降维",PCAfreqMatrix.shape)
#     #对PCAfreqMatrix计算出tf-idf矩阵
#     retfidf = transformer.fit_transform(PCAfreqMatrix)
#     print("计算出tf-idf矩阵",retfidf.shape)
#     print(retfidf,file=f4)
#     tfidf_train=retfidf.toarray()
#     print("tfidf_train.shape: ",tfidf_train.shape)
#
#     #Kmeans
#     km = cluster.KMeans(n_clusters=10, random_state=28,init='k-means++')
#     c = km.fit(tfidf_train)
#     print("Kmeans")
#     t = c.labels_
#     print(t,file=f3)
#     f3.close()
#     f4.close()
#     f5.close()











