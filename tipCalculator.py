# Print a message explaining the purpose of the program
message = "This program will calculate the tip in a restaurant"
print(message)

# Get the bill amount from the user
bill_without_tip = (input("What was the consumption today?: "))

# Convert the bill amount to a float
bill_without_tip = float(bill_without_tip)

# Get the tip percentage from the user
tip = float(input("How much tip do you want to leave in decimal: "))

# Calculate the total bill with tip
bill_with_tip = bill_without_tip + (tip * bill_without_tip)

# Print the total bill with tip
print("The total with tip is: ", bill_with_tip)
