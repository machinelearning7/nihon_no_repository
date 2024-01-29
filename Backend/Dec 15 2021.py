

age = 23

if age < 2:
    person = 'a baby'
if age >= 2:
    person = 'a toddler'
if age >= 13:
    person = 'a kid'
if age >= 20:
    person = 'an adult'
if age >= 65:
    person = 'an elder'

print(f"You are {person}.")
#exercise p. 85 took me a while to get it to work but it works!
#solved a/an issue by adding the article


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
#notice no indentation for final print message w/new line
#an if statement inside the for loop fixes issue related to being out of green peppers and changes msg

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
