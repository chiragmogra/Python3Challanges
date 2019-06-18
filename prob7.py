    
import os
ch=int(input("Enter an option from following:\n1.Create a new empty file\n2.create new empty multiple files\n3.Check whether a file is created or not\n4.Update access and modification time.\n5.update access and modification time of a file to that of another file\n"))
if ch==1:
    file1=input("enter name of file:-")
    path=open(file1,"a")
    path.close()
elif ch==2:
    fno=int(input("enter nos. of files you want to create:-"))
    for i in range(fno):
        file1=input("enter file "+str(i)+"name:-")
        path=open(file1,"a")
        path.close()
elif ch==3:
    fcheck=input("enter name of file:-")
    print("The file exists:"+str(path.isfile(fcheck)))
elif ch==4:
    floc=input("enter file name with loc. to change its modification time and curr time:-")
    os.utime(floc)
elif ch==5:
    lop=input("Enter File path from which upadated date and time is extracted\n")
    loc=input("Enter File path To Update date and time\n")
    os.utime(loc,(os.path.getmtime(lop),os.path.getmtime(lop)))
   