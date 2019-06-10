#!usr/bin/python3
import time
name =input("Enter Your Name ")
curr_tm_hour=int(time.localtime().tm_hour)
print(curr_tm_hour)
if curr_tm_hour>=5 and curr_tm_hour<12:
	print("Good Morning ",name)
elif curr_tm_hour>=12 and curr_tm_hour<17:
        print("Good Afternoon ",name)
elif curr_tm_hour>=17 and curr_tm_hour<21:
        print("Good Evening ",name)
elif curr_tm_hour>=21 or curr_tm_hour<5:
        print("Good Night ",name)

