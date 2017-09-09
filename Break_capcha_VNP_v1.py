import os
import requests
from PIL import Image
from base64 import decodestring
#Cấu hình chung

#Link nguồn capcha VNP
URL="http://naptien.vinaphone.com.vn/Home/GenerateCaptcha?_=1504926074759"

def save_capcha(so_luong):
	r = requests.get(URL)
	
	image = Image.fromstring('RGB',(width,height),decodestring(r.content))
	image.save("foo.png")
	a=
	return a
print(save_capcha(1))