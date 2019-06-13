#! /usr/bin/python3
from googlesearch import search
import webbrowser,time,qrcode
import pyzbar
link=[]
key=input("Enter what you want to search : ")

for i in search(key,stop=1) :
	print(i)
	link.append(i)
	time.sleep(1)
	qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=15, border=2 ) 
	qr.add_data(link) 
	qr.make(fit=True) 
	img = qr.make_image(fill_color="black", back_color="white") 
	img.save("MyQr2.png")


