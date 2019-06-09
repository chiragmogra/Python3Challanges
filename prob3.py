#!usr/bin/python3
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
l1=[]
l2=[]
for i in adhoc:
	if i>5 :
		print(i)
		l1.append(i)
	if i<=2 :
		print(i)
		l2.append(i)
print("List of values greater than 5",l1)
print("List of values less than or equals to 2",l2)
		

