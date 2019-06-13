#! /usr/bin/python3
from googlesearch import search
import webbrowser,time,qrcode
import pyzbar
link=[]
n=1
key=input("Enter what you want to search : ")

for i in search(key,stop=3) :
	link.append(i)
for i in link :
	qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=2 ) 
	qr.add_data(i) 
	qr.make(fit=True) 
	code = qr.make_image(fill_color="black", back_color="white") 
	code.save(f"SearchResult{n}.png")
	n=n+1


