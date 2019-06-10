#!usr/bin/python3
import datetime
name=input("Enter Your Name ")
age=int(input("Enter Your Age "))
curr_year=(datetime.datetime.now()).year
year=95+curr_year-age
print("When your age is 95 than that year will be ",year)
