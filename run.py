import random


# Logo for the game. Generated with: https://www.ascii-art-generator.org/
print(
    """
 _____  _ _                 _ _       _    _                                         
|  __ \(_) |               | ( )     | |  | |                                        
| |__) |_| | ____ _ _ __ __| |/ ___  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  /| | |/ / _` | '__/ _` | / __| |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | \ \| |   < (_| | | | (_| | \__ \ | |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  \_\_|_|\_\__,_|_|  \__,_| |___/ |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                                          __/ |                      
                                                         |___/        
    """
)

# Welcoming the player to the game
print("\nWelcome to Rikard's Hangman!")
name = input("Enter your name:")
print(f"Good Luck, {name}!")


def get_word():
    """
    Gets a random word from words.txt
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    print(random_word.upper())


get_word()


def show_rules():
    print(
        """
        Choose a letter from A to Z. If it's not in the word, you loose a life.\n
        If it's correct it will show in the word.\n
        The game is over if you loose all lives.\n
        You win if you get all letters right!
        """
        )
    input("Press enter to return to menu")
    menu()


def main():
    """
    Runs the game
    """               


def menu():
    """
    Presents choices to the player
    """
    print("Press 1 to start the game")
    print("Press 2 to show the rules")
    print("Press 3 to set difficulty")
    choice = input("Enter number:")
    if choice == "1":
        main()
    elif choice == "2":
        show_rules()
    elif choice == "3":
        print("choose_level")
    else:
        print("Please choose 1,2 or 3.")
        menu()


menu()


