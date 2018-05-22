import os
import json


def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def file_name(path):
    for root, dirs, files in os.walk(path):
        cnt = 0
        tot = len(files)
        for file in files:
            alter(file, "t", "t")
            cnt += 1
            print("%s, (%d/%d)" % (file, cnt, tot))


def main():
    #path = os.getcwd()
    #file_name
    f =open("59877.json","r+",encoding = 'utf-8')
    s = f.read()
    s = s.replace("xa0"," ")
    print(s)




if __name__ == '__main__':
    main()
    # print()
    # alter("59914.json","t"," ")
    # info = json.load(open("59914.json", 'r'))