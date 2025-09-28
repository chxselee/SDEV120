# Program to ask the user for 15 numbers and check if they are even or odd

# Create an empty list to store numbers
numbers = []

# Collect 15 numbers from the user
for i in range(15):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

# Loop through the list and check if each number is even or odd
for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")
