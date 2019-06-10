#pgm for greeting you; only you have to enter yr name

import datetime

t = datetime.datetime.now()
curhr = t.hour

n = input("Enter your name : " )


if t.hour<12 :
	print(f"Good morning {n}")
elif t.hour<16 :
	print(f"Good afternoon {n}")
elif t.hour<20 :
	print(f"Good evening {n}")
else :
	print(f"Good night {n}")
