adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
five=[]
two=[]

for i in adhoc :
	if i>5 :
		five.append(i)
	elif i<=2 :
		two.append(i)


print("\nList of numbers greater than 5 in the predefied list : ",five)
print("\nList of numbers less than or equal to the predefined list : ",two)
