import random

scoreboard = {"Player": 0, "Computer": 0, "Ties": 0}

def divider():
    print("_________________________________________________________________")
    print("=================================================================")
    print()

def game():
        divider()
        player_choice = input("Enter one of the following... Rock, Paper, or Scissors: ").lower()

        rps = ["rock", "paper", "scissors"]
        if player_choice not in rps:
            print("Invalid input")
            input("Press Enter to try again... ")
            game()
        else:
            computer_choice = random.choice(rps)
            print("Computer has chosen: " + computer_choice.capitalize())

            # Tie Game
            if player_choice == computer_choice:
                print("Tie Game!")
                scoreboard["Ties"] += 1
            # Player Win
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "paper" and computer_choice == "rock") or \
                 (player_choice == "scissors" and computer_choice == "paper"):
                print("Player Wins!")
                scoreboard["Player"] += 1
            # Computer Win
            else:
                print("Computer Wins!")
                scoreboard["Computer"] += 1

def replay():
    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again == "y":
            return True
        elif play_again == "n":
            return False
        else:
            print("Invalid input, please enter 'y' or 'n'")

while True:
    game()
    print(scoreboard)
    if not replay():
        divider()
        print("Thanks for playing!")
        print("Final Score: " + str(scoreboard))
        break