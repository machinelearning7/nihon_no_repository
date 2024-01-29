



name = input("what is your name: ")
print( name )
age = int(input("How old are you? "))
year = str((2021 - age)+100)
print(name + " will be 100 years old in the year " + year)

Name = input("What is your name: ")
Age = int(input('how old are you: '))
Thisyear = int(input("what year is it today: "))
Year = str((Thisyear - Age)+100) 
print(Name + " will be 100 years old in the year " + Year)

import datetime

now = datetime.datetime.now()
currentyear = now.year
name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
hundredIn = ((100 - age) + currentyear)

print ('Hi '+name + ', you will be 100 years old in ' + str(hundredIn))

from datetime import date
name = input("What is yr name: ")
age = input("Enter age: ")

date = date.today()
print(name + " you will be 100 years old in " + str(int(date.year) + 100 - int(age)))