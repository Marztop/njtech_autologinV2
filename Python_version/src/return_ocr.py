import ddddocr

captcha = ddddocr.DdddOcr()

with open('C:\\Users\\Marztop\\Desktop\\ca.jpg','rb') as img:
    imgbyte=img.read()
res=captcha.classification(imgbyte)
print(res)