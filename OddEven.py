
message = "Hello, this program will tell you if the number is even or odd"
print(message)

# We ask the user to input a number and store it as a string
number = input("Choose a number: ")

# We cast the string to an integer so we can perform arithmetic operations on it
number = int(number)

# We check if the number is even by checking if the remainder of the division by 2 is 0
if number % 2 == 0:
    # If the remainder is 0, we print that the number is even
    print("It's even")
else:
    # If the remainder is not 0, we print that the number is odd
    print("It's odd")
