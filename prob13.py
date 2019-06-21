# please install pyttsx3 module to run this program
#!/usr/bin/python3
import datetime
import pyttsx3
now=datetime.datetime.now()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 120)
usrname=input("please enter your name:-")
if now.hour>=5 and now.hour<12:
	engine.say("Good Morning"+str(usrname))
elif now.hour>=12 and now.hour<15:
	engine.say("Good Afternoon"+str(usrname))
elif now.hour>=15 and now.hour<20:
	engine.say("Good Evening"+str(usrname))
else:
	engine.say("Good Night"+str(usrname))
engine.runAndWait()
print("Installed modules in these module are:\n1.add()\n2.sorting\n3.datetime\n4.pyttsx3")
def add():
	num1=int(input("enter 1st no."))
	num2=int(input("enter 2nd no."))
	print(x+y)
def sorting():
	num=[]
	input_string=input("enter elements of list with spaces for sorting")
	num=input_string.split()
	num.sort()
	print(num)
	
