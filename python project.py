import time

def print_pause(x):
    print(x)
    time.sleep(1)
# GAME BEGINNING FUNCTION
def game_beginning():
    print_pause("You find yourself in front of a vampire mansion.")
    print_pause("There are two paths in front of you.")
    print_pause("You can either knock on the door of the house or enter the cave.")
# VAMPIRE MASSION
def vampire_mansion(total_score):
    print_pause("You knock on the door of the house.")
    print_pause("A vampire opens the door and invites you inside.")
    print_pause("What will you do?")
    choice = input("1. Follow the vampire inside.\n2. Go away.\n")
    if choice == '1':
        print_pause("You follow the vampire inside and find a treasure chest!")
        total_score += 10
    elif choice == '2':
        print_pause("You run away safely. But the adventure continues...")
        total_score += 5
    else:
        print_pause("Invalid choice. Try again.")
        return vampire_mansion(total_score)  
    print_pause(f"Your score is {total_score}.")
    return total_score
# CAVE MISSION
def cave(total_score):
    print_pause("You enter the dark cave.")
    print_pause("It's cold and eerie.")
    print_pause("What will you do?")
    choice = input("1. Keep going deeper into the cave.\n2. Turn back and leave the cave.\n")
    if choice == '1':
        print_pause("You go deeper into the cave and find a hidden passage!")
        total_score += 10
    elif choice == '2':
        print_pause("You leave the cave and return to the mansion.")
        total_score += 5
    else:
        print_pause("Invalid choice. Try again.")
        return cave(total_score)  
    print_pause(f"Your score is {total_score}.")
    return total_score
# GAME MISSION
def play_game():
    total_score = 0
    game_beginning()
    path_choice = input("Which path will you choose?\n1. Knock on the door.\n2. Enter the cave.\n")
    if path_choice == '1':
        total_score = vampire_mansion(total_score)
    elif path_choice == '2':
        total_score = cave(total_score)
    else:
        print_pause("Invalid choice. Try again.")
        return play_game()  

    print_pause(f"Final score: {total_score}")
    if total_score != 10:
        print_pause("Congratulations! You completed the adventure successfully!")
    else:
        print_pause("You failed try again")

    play_again = input("Would you like to play again? (yes/no)\n").lower()
    if play_again == 'yes':
        play_game()
    else:
        print_pause("Thank you for playing! Goodbye!")

play_game()
