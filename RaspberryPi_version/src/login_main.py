debug_mode = False


import paramiko
import time
import requests
import re
import ddddocr


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.1.1', port=22, username='root', password='admin')

def send_command(command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    if debug_mode == True:
        try:
            if stdout.read():
                print(stdout.read().decode('utf-8'))
            else:
                print(stderr.read().decode('utf-8'))
        except Exception:
            print(Exception)

def login():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
    }
    session=requests.Session()

    def get_args(session):
        res = session.get(r'https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232')
        text = res.text
        if debug_mode == True:
            print(text)
        lt=re.findall('(?<=name="lt" value=").*',text)[0].split('"')[0]
        execution=re.findall('(?<=name="execution" value=").*',text)[0].split('"')[0]
        url_param = re.findall('(?<=action=").*', text)[0].split('"')[0]
        post_url = 'https://u.njtech.edu.cn'+url_param
        #jsessionid=re.findall('(?<=jsessionid=).*',url_param)[0].split('?')[0]
        return lt,execution,post_url

    def get_captcha(session):
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
        captcha = ddddocr.DdddOcr()
        result=captcha.classification(res.content)
        return result
    
    lt,execution,post_url=get_args(session)
    captcha=get_captcha(session)
    params = {
        'username': 'username',
        'password': 'password',
        'captcha': captcha,
        'channelshow': '中国移动',
        'channel': '@cmcc',
        'lt': lt,
        'execution': execution,
        '_eventId': 'submit',
        'login': '登录'
    }
    login_response = session.post(url=r'https://u.njtech.edu.cn/cas/login?service=https%3A%2F%2Fu.njtech.edu.cn%2Foauth2%2Fauthorize%3Fclient_id%3DOe7wtp9CAMW0FVygUasZ%26response_type%3Dcode%26state%3Dnjtech%26s%3Df682b396da8eb53db80bb072f5745232', params=params, headers=headers)
    session.close()
    return 0


if __name__ == '__main__':
    send_command('cd /sbin/;./ifup wan')
    send_command('cd /sbin/;./ifdown wan2')
    send_command('cd /sbin/;./ifdown wan3')
    time.sleep(2)
    login()

    send_command('cd /sbin/;./ifdown wan')
    send_command('cd /sbin/;./ifup wan2')
    time.sleep(2)
    login()

    send_command('cd /sbin/;./ifdown wan2')
    send_command('cd /sbin/;./ifup wan3')
    time.sleep(2)
    login()

    send_command('cd /sbin/;./ifup wan')
    send_command('cd /sbin/;./ifup wan2')
    send_command('cd /usr/sbin;./mwan3 stop')
    send_command('cd /usr/sbin;./mwan3 start')
    send_command('cd /usr/sbin;./mwan3 restart')

ssh_client.close()