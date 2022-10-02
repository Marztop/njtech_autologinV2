import requests
import os
from http import client

client.HTTPConnection._http_vsn=10
client.HTTPConnection._http_vsn_str='HTTP/1.0'

self_path=os.path.dirname(os.path.abspath(__file__))

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'u.njtech.edu.cn'
}

res = requests.get('https://u.njtech.edu.cn/cas/captcha.jpg',stream=True)
#print(res.text)
with open(self_path+'\\captcha.jpg','wb') as img:
    img.write(res.content)