print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")


while True:
    first_number = input("n\First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# This works and gives a zero division error if divided by zero.