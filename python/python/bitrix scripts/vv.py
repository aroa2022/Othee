import base64
import base64
import requests

#f=  open("2.jpg", 'wb') 
#f.write(requests.get('https://buomsoo-kim.github.io/data/images/2018-04-16/5.PNG').content)



with open('1.png','rb') as f: 
    en= base64.b64decode(f.read())

print(en)