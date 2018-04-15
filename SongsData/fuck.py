import os


def file_name(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)

        print(root)  #当前目录路径
        print(files)  #当前路径下所有非目录子文件


def main():
    path = os.getcwd()
    file_name(path)


if __name__ == '__main__':
    main()