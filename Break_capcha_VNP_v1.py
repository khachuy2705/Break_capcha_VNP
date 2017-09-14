import os
import cv2
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))
#Cài đặt PIL bằng pip3 install Pillow
from PIL import Image
import base64
from shutil import copyfile
import random

#Cấu hình chung
capcha_path='D:\Lab_Zone\Python\Break_capcha_VNP\capcha_saved\\'
#Link nguồn capcha VNP
URL= 'http://naptien.vinaphone.com.vn/Home/GenerateCaptcha?_=1504926074759'
kho_cap_cha= dir_path + "\\captcha_storaged\\"
da_xu_ly=dir_path+'\\da_xu_ly\\'
dang_xu_ly=dir_path+'\\dang_xu_ly\\'
sample=dir_path+'\\sample\\'

def chuoi_ngau_nhien(so_ky_tu):
	ngau_nhien=""
	for i in range(0,so_ky_tu):
		ngau_nhien=ngau_nhien+str(chr(random.randint(97,122)))+str(chr(random.randint(48,57)))+str(chr(random.randint(65,90)))
	return ngau_nhien

#Hàm lấy ảnh về từ VNP
def save_capcha(so_luong):
	for i in range(1,so_luong):
		r = requests.get(URL)
		png_recovered = base64.decodebytes(r.content)
		f = open(kho_cap_cha+"/"+chuoi_ngau_nhien(6)+".png", "wb")
		f.write(png_recovered)
		f.close()
		print("Lay thanh cong capcha thu "+str(i))
	return "OK"

def reduce_noise(filename):
	random_name= chuoi_ngau_nhien(3)
	copyfile(filename, dang_xu_ly+random_name+'.png')
	filename2=dang_xu_ly+random_name+'.png'
	img = cv2.imread(filename2)
	dst = cv2.fastNlMeansDenoisingColored(img,None,29,21,50,10)
	cv2.imwrite(filename2, dst)
	img = Image.open(filename2).convert('L')
	img = img.point(lambda x: 0 if x<128 else 255, '1')
	img.save(da_xu_ly+'_result.png')
	os.remove(filename2)

def list_storage_file():
	for file in os.listdir(kho_cap_cha):
		if file.endswith(".png"):
			print(os.path.join("/mydir", file))

# print(list_storage_file)
# reduce_noise(kho_cap_cha+'_9_.png')
# print(dir_path)
# save_capcha(1000)