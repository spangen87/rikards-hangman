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

#Welcoming the player to the game
print("\nWelcome to Rikard's Hangman!")
name = input("Enter your name:")
print(f"Good Luck, {name}!")


def menu():
    """
    Presents choices to the player
    """
    print("Press 1 to start the game")
    print("Press 2 to show the rules")
    print("Press 3 to set difficulty")
    choice = input("Enter number:")
    if choice == "1":
        print("start_game")
    elif choice == "2":
        print("show_rules")
    elif choice == "3":
        print("choose_level")
    else:
        print("Please choose 1,2 or 3.")            

menu()



def get_word():
    """
    Gets a random word from words.txt
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    print(random_word.upper())

get_word()

               
