import datetime

n=input("Enter your Name : ")
a=int(input("Enter your age : "))
y=datetime.datetime.now()
p_y=y.year

if a<95 :
	p_a = 95-a
	f_y = p_y+p_a
	print(n+" you will be 95 year old till : ",f_y) 
elif a>95 :
	print(n+" you are already 95 yrs old.")

else :
	print(n+" you are in your 95th yr age.")
 
	
