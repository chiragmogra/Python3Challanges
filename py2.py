#! usr/bin/python3                                                                                                                                                     
import googlesearch                                                                                                                                                     
ch=input("Enter search things")                                                                                                                                         
links=googlesearch.search(ch,stop=10)                                                                                                                                   
link=[i for i in links]                                                                                                                                                 
l_file=open("link.txt","w")                                                                                                                                             
for i in link:                                                                                                                                                          
        l_file.write(i)                                                                                                                                                 
        l_file.write("\n")                                                                                                                                                                      