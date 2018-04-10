import time
import hashlib
import requests
from bs4 import BeautifulSoup
import re
orderno = "DT20180410120342axUH7PNS"
secret = "37688b714a0c5d0e794c5e6bb5058ee3"

ip = "dynamic.xiongmaodaili.com"
port = "8088"

# ip_port = ip + ":" + port
ip_port = '222.78.232.246:34168';

timestamp = str(int(time.time()))                # 计算时间戳
txt = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
txt = txt.encode()

md5_string = hashlib.md5(txt).hexdigest()                 # 计算sign
sign = md5_string.upper()                              # 转换成大写
# print(sign)
auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp

# print(auth)
proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36',
           "Authorization": auth}

if __name__ == '__main__':
	r = requests.get("http://music.163.com/song?id=393695", headers=headers, proxies=proxy)
	print(r.status_code)
	r = BeautifulSoup(r.text, 'lxml').find('script', attrs={"type": "application/ld+json"}).text
	pat = re.compile(r'\"images\": \[.*\]')
	#print(type(r))
	print(pat.findall(r)[0][12:-2])
	