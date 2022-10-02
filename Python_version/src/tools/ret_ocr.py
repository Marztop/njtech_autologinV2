import ddddocr
import os

img_path=os.path.dirname(os.path.abspath(__file__))+'\\captcha.jpg'
captcha = ddddocr.DdddOcr()

with open(img_path,'rb') as img:
    imgbyte=img.read()
res=captcha.classification(imgbyte)
print(res)
os.system('PAUSE')