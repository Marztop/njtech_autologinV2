

import os
import requests

file_path=os.path.dirname(os.path.abspath(__file__))+'\\raw.txt'

page = requests.get('https://i.njtech.edu.cn/')
text = page.text

with open(file_path,'w',encoding='utf-8') as f:
    f.write(text)

