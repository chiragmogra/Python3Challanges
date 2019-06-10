#!usr/bin/python3
import os
import subprocess
uno=int(input("please enter no of users"))
ulist=[]
i=0
while i<uno:
	uname=input("Enter User Name ")
	if uname.isalpha():
		print("uname is valid")
		ulist.append(uname)
		i+=1
	else:
		print("uname is not valid (It does not consist numbers)")

for i in ulist:
	pas="hello"+i
	comf="useradd -p $(openssl passwd -1 "+pas+") "+i
	os.system(comf)
	print(uname," user added ")

