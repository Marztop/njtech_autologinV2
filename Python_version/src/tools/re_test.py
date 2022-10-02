import re
import os

file_path=os.path.dirname(os.path.abspath(__file__))+'\\raw.txt'
with open(file_path,'r',encoding='utf-8') as f:
    text=f.read()

lt=re.findall('(?<=name="lt" value=").*',text)[0].split('"')[0]
execution=re.findall('(?<=name="execution" value=").*',text)[0].split('"')[0]
url_param = re.findall('(?<=action=").*', text)[0].split('"')[0]
jsessionid=re.findall('(?<=jsessionid=).*',url_param)[0].split('?')[0]

print(jsessionid)