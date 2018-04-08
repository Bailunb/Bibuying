# Bibuying

由于彭先生起了“十度”这个名字

我们顺势起了个“必不应”，大家都是假的搜索引擎

## 要求

第一次小组项目作业：
Lucene倒排检索，给定一个不少于10k条的文本数据集，实现创建索引和检索功能。
加分项：中文语料、检索界面web化， 或借助solr，elastic等工具。
Deadline：4月15日。

## 项目环境

python 3.6 (Anaconda, windows 64)
pycharm

## 数据来源

从网易云爬歌手的热门50首歌

分类分别为

- 华语男歌手
- 华语女歌手
- 华语组合/乐队

每个分类里有100个热门歌手，每个歌手50首歌

	3 * 100 * 50 = 15000 首歌

数据量应该符合要求的

// 待续

——by cww

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

[python爬取网易云歌词](https://www.cnblogs.com/Beyond-Ricky/p/6757954.html)

[django教程 | 菜鸟教程](http://www.runoob.com/django/django-tutorial.html)

[Elasticsearch 权威指南](https://es.xiaoleilu.com/index.html)