# Bibuying

we are [here](https://github.com/BibuyingTeam/Bibuying.git)

由于彭先生起了“十度”这个名字

我们顺势起了个“必不应”，大家都是假的搜索引擎

华东师范大学 计算机科学与软件工程学院

指导老师：姚俊杰

陈伟文 10152510217

徐洪义

盛俊杰

## 要求

第一次小组项目作业：

Lucene倒排检索，给定一个不少于10k条的文本数据集，实现创建索引和检索功能。

加分项：中文语料、检索界面web化， 或借助solr，elastic等工具。

Deadline：4月15日。

## 项目环境

- windows 64
- Anaconda(py3.6)
- pycharm

## 数据来源

// this part is edited by cww

从网易云爬歌手的热门50首歌

分类分别为

- 华语男歌手
- 华语女歌手
- 华语组合/乐队

每个分类里有100个热门歌手，每个歌手50首歌

`3 * 100 * 50 = 15000 首歌`

数据量应该符合要求的10k

流程：

1. 获取歌手id表，存入`artist_id.txt`内 
2. 获取每个歌手的50首热门歌曲id 
3. 根据歌曲id爬歌词保存json文件

### 文件说明

`main.py`：主要过程代码都在这

`artist_id.py`: 歌手id文件，为`get_artist_id()`写出的文件

`web.html`：爬取网页源码，先存在这看一眼，该文件未push

### 基本操作

定义`get_soup()`爬取html：
```python
def get_soup(web_url):
	print(web_url)
	req = urllib.request.Request(url=web_url, headers=headers)
	# print(req)
	web_page = urllib.request.urlopen(req)
	data = web_page.read()
	soup = BeautifulSoup(data, 'lxml')
	f.write(soup.prettify())
	return soup
```

### 爬取歌手id

以华语男歌手为例，url：`http://music.163.com/discover/artist/cat?id=1001`
内有标签`<a class="nm nm-icn f-thide s-fc0" href=" /artist?id=3681" title="李志的音乐">`

于是有了下面两行
```python
ids = soup.find_all('a', attrs={"class": "nm nm-icn f-thide s-fc0"})
pattern = re.compile(r'id=\d+')
```
找到所有标签然后用正则表达式得到id

结果存在`artist_id.txt`中，如下：

![artist_id](doc/pic/artist_id.png)

### 根据id获取歌单

直接爬`http://music.163.com/#/artist?id=3681`有个问题，爬出来一堆js脚本，这个动态加载的页面

知乎上[这里](https://www.zhihu.com/question/21471960)发现个技巧，右击检查元素发现

![](doc/pic/song_id.png)

这里有个请求可以得到歌单，其header如下

    Request URL: http://music.163.com/artist?id=3681
    Request Method: GET
    Status Code: 200 OK
    Remote Address: 223.252.199.66:80
    Referrer Policy: no-referrer-when-downgrade
    
emmmmm，把`#`扔掉就完事了

这里就面临一个选择，是把id存在一个本地文件里然后一行一行读来操作或者是直接在这里做到底，歌手歌名歌词搞完。

对接json文件，封面 + 歌词 + 音频链接 + 歌名 + 歌手名

### 歌曲封面

封面有个图片url，可以爬歌曲页面来获取html中的图片url

```python
def get_pic(song_id):
	song_url = 'http://music.163.com/song?id=%s' % str(song_id)
	soup = get_soup(song_url)
	st = soup.find('script', attrs={"type": "application/ld+json"}).text
	pat = re.compile(r'\"images\": \[.*\]')
	return pat.findall(st)[0][12:-2]
```

### 歌词

歌词找了半天，网易云有官方的接口

`http://music.163.com/api/song/lyric?id=%s&lv=1&kv=1&tv=-1`

直接get会得到这样一坨

![lyric](doc/pic/lyric.png)

需要正则表达式一通操作，如下

```
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
```

### 中文分词

将歌词分词，以供后面倒排索引使用。调用一下`jieba`，挺easy的

```python
def get_words(lyric):
	word_lst = []
	seg_list = jieba.cut(lyric, cut_all=True)
	for word in seg_list:
		if word != '' and not '\n' in word:
			word_lst.append(word)
	return word_lst
```

### 其他信息

歌手名，歌名在歌手歌单页面可以爬到
网易云有外链播放器功能，我想web搭建的时候，可以嵌一个

![](doc/pic/player.png)

```
<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 
src="//music.163.com/outchain/player?type=2&id=26508240&auto=0&height=66"></iframe>
```

只需要传入歌曲id就可以了

### 数据打包

打包为一个json文件，文件名为歌曲id，放在`SongsData`文件夹中

```python
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
```

### ip问题

爬了10分钟之后发现自己电脑无法访问网易云了，代码没有写错，而是网易云封了我的ip（10分钟访问几千次可能要封）

于是乎，第二天在一个http代理的网站上买了1k个ip，爬废了一个ip换下一个

`get_soup()`改为:

```python
def get_soup(web_url):
	# html_file = open("web.html", "w", encoding='utf-8')
	if not 'lyric' in web_url: print(web_url)
	proxy = {"http": "http://" + ips[0], "https": "https://" + ips[0]}
	req = requests.get(url=web_url, headers=headers, proxies=proxy)
	soup = BeautifulSoup(req.text, 'lxml')
	# html_file.write(soup.prettify())
	return soup
```

`headers`加入`"Authorization": get_ips.auth`，为http运营商提供的接口

多了一个`get_ips.py`，ip的各种验证之类

![](doc/pic/ips.png)

### 数据完成

从9日晚上到10日晚上（爬的过程不是写代码的过程），

终于在凌晨看见了如下输出

![](doc/pic/over.png)

300个歌手，应该是0到299，我还刻意写了`for i in range(0, 301)`，蠢了蠢了

![](doc/pic/songdata.png)

共爬到13k的数据，数量级符合要求了，剩下的便是倒排索引和web展示了

// 2018/04/11


## 数据索引

由于前面使用的py进行操作，这里方便起见统一使用了`elastic`的python接口`elasticsearch`.



// add here

——by xhy

## 检索界面

核心功能两个页面，搜索结果目录页和details页，有心情再搞个搜索主页

// add here

——by sjj

## 后记

感谢感谢感谢balabala

## 参考文献

[NetCloud Music](http://music.163.com)

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

[python爬取网易云歌词](https://www.cnblogs.com/Beyond-Ricky/p/6757954.html)

[python 爬去js生成的网页内容](https://www.zhihu.com/question/21471960)

[熊猫代理HTTP](http://www.xiongmaodaili.com/)

[ElasticSearch py](https://pypi.python.org/pypi/elasticsearch/2.2.0)

[django教程 | 菜鸟教程](http://www.runoob.com/django/django-tutorial.html)