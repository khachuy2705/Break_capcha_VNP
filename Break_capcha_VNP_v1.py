import os
import requests

#Cài đặt PIL bằng pip3 install Pillow
from PIL import Image
import base64
from base64 import decodestring
#Cấu hình chung
capcha_path='D:\Lab_Zone\Python\Break_capcha_VNP\capcha_saved\\'
#Link nguồn capcha VNP
URL="http://naptien.vinaphone.com.vn/Home/GenerateCaptcha?_=1504926074759"

#Hàm lấy ảnh về từ VNP
def save_capcha(so_luong):
	for i in range(1,so_luong):
		r = requests.get(URL)
		png_recovered = base64.decodestring(r.content)
		f = open(capcha_path+"_"+str(i)+"_"+".png", "wb")
		f.write(png_recovered)
		f.close()
	return "OK"

# print(save_capcha(1000))