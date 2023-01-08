
import random

computer_choice = random.randint(0,101)

counter = 0

while True:
    human_choice = int(input("Please enter a number between 1-100: "))
    counter += 1
    if computer_choice == human_choice:
        print("You Won in: ", counter, "guesses")
        break
    elif human_choice > computer_choice:
        print("Enter a smaller number")
    elif human_choice < computer_choice:
        print("Enter a larger number")
    

