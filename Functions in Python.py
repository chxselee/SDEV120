# Function definition
def greater_than(x, y):
    # Check if x is greater than y
    if x > y:
        return True
    else:
        return False

# Main section of the program
a = 10
b = 6

# Call the function and store the result in a variable
result = greater_than(a, b)

# Print the output
print("The statement", a, "is greater than", b, "is", result)
