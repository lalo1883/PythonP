import random

def play_rpt():
    # options
    options = ["rock", "paper", "scissors"]

    # choose option for the computer
    computer_option = random.choice(options)

    # ask player for option
    player_option = input("Rock, paper, or scissors? ").lower()

    # check if player's option is valid
    if player_option not in options:
        print("Invalid option, try again.")
        return

    # determine winner
    if player_option == computer_option:
        print("Draw.")
    elif player_option == "rock" and computer_option == "scissors":
        print("You won.")
        return "player"
    elif player_option == "paper" and computer_option == "rock":
        print("You won.")
        return "player"
    elif player_option == "scissors" and computer_option == "paper":
        print("You won.")
        return "player"
    else:
        print("You lost.")
        return "computer"

# start game
print("Welcome to Rock, Paper, Scissors.")

# counters
game_count = 0
player_wins = 0
computer_wins = 0

# play while player wants to
while True:
    winner = play_rpt()
    game_count += 1

    if winner == "player":
        player_wins += 1
    elif winner == "computer":
        computer_wins += 1

    # ask player if they want to play again
    play_again = input("Do you want to play again? [y/n] ").lower()
    if play_again != "y":
        break

# show final results
print(f"Thank you for playing. You played {game_count} games.")
print(f"You won {player_wins} and the computer won {computer_wins}.")
