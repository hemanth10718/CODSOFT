import random

options = ("rock", "paper", "scissors")
running = True  

def display_instructions():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions:")
    print("1. Enter your choice (rock, paper, or scissors) when prompted.")
    print("2. The computer will randomly select its choice.")
    print("3. The winner is determined based on the following rules:")
    print("     a) Rock beats scissors")
    print("     b) Scissors beat paper")
    print("     c) Paper beats rock")
    print("4. If both choices are the same, it's a tie.")
    print("5. You can play multiple rounds. Enter 'y' to play again or 'n' to quit.")
    print("Let's start!\n")

def get_player_choice():
    player = None
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        if player not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
    return player

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors"):
         print("You win!")
    elif (player == "paper" and computer == "rock"):
         print("You win!")
    elif (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

display_instructions()

while running:
    player = get_player_choice()
    computer = random.choice(options)

    print(f"\nPlayer: {player.capitalize()}")
    print(f"Computer: {computer.capitalize()}")

    result = determine_winner(player, computer)
    print(result)

    play_again = input("\nWould you like to play another round? (yes/no): ").lower()
    while play_again not in ('yes', 'no'):
        play_again = input("Invalid input. Would you like to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        running = False

print("Thanks for playing, Have a good day!")
