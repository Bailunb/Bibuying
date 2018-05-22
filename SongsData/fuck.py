import os


def file_name(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)

        print(root)  #当前目录路径
        print(files)  #当前路径下所有非目录子文件


def main():
    #path = os.getcwd()
    #file_name
    f =open("59877.json","r+",encoding = 'utf-8')
    s = f.read()
    s = s.replace("xa0"," ")
    print(s)



if __name__ == '__main__':
    main()