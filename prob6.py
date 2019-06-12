#!usr/bin/python3
print("Enter 1 for display file content")
print("Enter 2 for display content of a multiple files")
print("Enter 3 for create a file")
print("Enter 4 for create multiple file")
print("Enter 5 for enter content into a file(overrite) like 'cat a>b' ")
print("Enter 6 for enter content into a file(append) like 'cat a>>b' ")
ch=int(input())
if ch==1:
	f_loc=input("Enter file name with loc ")
	fp=open(f_loc,"r")
	print(fp.read())
	fp.close()
elif ch==2:	
	f_li=[]
	while True:
		op=int(input("\tenter 1 for enter file name \n\t 2 for show the data of all entered files\n\t 3 for exit"))
		if op==1:
			f_loc=input("\tEnter file name with loc ")
			f_li.append(f_loc)
		
		elif op==2:
			for i in f_li:
				fp=open(i,"r")
				print(fp.read())
				fp.close()
		elif op==3:
			break
elif ch==3:
	f_loc=input("Enter file name to create  ")
	fp=open(f_loc,"x")
	fp.close()
elif ch==4:	
	f_li=[]
	while True:
		op=int(input("\tenter 1 for enter file name \n\t 2 for create all files and then exit\n\t "))
		if op==1:
			f_loc=input("\tEnter file name with loc where you want to create ")
			f_li.append(f_loc)
		
		elif op==2:
			for i in f_li:
				fp=open(i,"x")
				print(fp.read())
				fp.close()
				break

elif ch==5:
	f_loc=input("Enter file name with loc ")
	fp=open(f_loc,"w")
	data=input("Enter data for overwrite ")
	fp.write(data)
	fp.close()
elif ch==6:
	f_loc=input("Enter file name with loc ")
	fp=open(f_loc,"a")
	data=input("enter data for appending the data ")
	fp.write(data)
	fp.close()
	
