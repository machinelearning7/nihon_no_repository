name = input("What is your name: ")
print(name)
age = int(input("How old are you? "))
year = str((2021 - age) + 100)
print(name + " will be 100 years old in the year " + year)



from datetime import date
name = input("What is your name? ")
age = input("Enter your age: ")

date = date.today()
print(name + " you will be 100 years old in " + str(int(date.year) + 100 - int(age)))