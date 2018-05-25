import os
import json


def remove_extra_quotes(file):
    file_data = ''
    with open(file, "r", encoding="utf-8") as f:
        line_no = 0
        for line in f:
            line_no += 1
            if line_no == 5:
                new_line = list(line)
                # print(new_line)
                idx = []
                for i in range(len(line)):
                    if line[i] == '"': idx.append(i)
                if len(idx) == 4: continue
                # print(idx)
                idx = idx[1:-1]
                #print(idx)
                for i in idx:
                    new_line[i] = '\''
                line = ''.join(new_line)

            # print(line_no, ' ', line, end='')
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def alter(file, old_str, new_str):
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
            if file == 'fuck.py': continue
            remove_extra_quotes(file)
            # alter(file, ", \"pic_url", ",\n\"pic_url")
            cnt += 1
            print("%s, (%d/%d)" % (file, cnt, tot))


def main():
    path_name = os.getcwd()
    # print(path_name)
    file_name(path_name)


if __name__ == '__main__':
    # main()
    remove_extra_quotes('139351.json')
    pass