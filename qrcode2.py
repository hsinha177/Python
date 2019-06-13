#!/usr/bin/python3
import qrcode
import matplotlib.pyplot as plt 
qr = qrcode.QRCode( version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4 ) 
qr.add_data('Some data') 
qr.make(fit=True) 
img = qr.make_image(fill_color="black", back_color="white")
img.save("MyQr.png")
plt.imread("MyQr.png")
plt.show()


