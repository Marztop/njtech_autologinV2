import requests
import re
import os
import ddddocr
import autologin_config

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
}
self_path=os.path.dirname(os.path.abspath(__file__))
session=requests.Session()

def get_args():
    res = session.get(r'https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232')
    text = res.text
    #print(text)
    lt=re.findall('(?<=name="lt" value=").*',text)[0].split('"')[0]
    execution=re.findall('(?<=name="execution" value=").*',text)[0].split('"')[0]
    url_param = re.findall('(?<=action=").*', text)[0].split('"')[0]
    post_url = 'https://u.njtech.edu.cn'+url_param
    #jsessionid=re.findall('(?<=jsessionid=).*',url_param)[0].split('?')[0]
    return lt,execution,post_url

def get_captcha():
    from http import client
    client.HTTPConnection._http_vsn=10
    client.HTTPConnection._http_vsn_str='HTTP/1.0'
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'u.njtech.edu.cn'
    }
    res = session.get('https://u.njtech.edu.cn/cas/captcha.jpg',headers=headers)
    with open(self_path+'\\captcha.jpg','wb') as img:
        img.write(res.content)
    captcha = ddddocr.DdddOcr()
    with open(self_path+'\\captcha.jpg','rb') as img:
        imgbyte=img.read()
        result=captcha.classification(imgbyte)
    return result

def main():
    lt,execution,post_url=get_args()
    captcha=get_captcha()
    params = {
        'username': autologin_config.username,
        'password': autologin_config.password,
        'captcha': captcha,
        'channelshow': autologin_config.channelshow,
        'channel': autologin_config.channel,
        'lt': lt,
        'execution': execution,
        '_eventId': 'submit',
        'login': '登录'
    }
    login_response = session.post(url=r'https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232', params=params, headers=headers)
    return 0

if __name__ == '__main__':
    main()