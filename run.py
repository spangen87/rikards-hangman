import random
import os

# System call
os.system("")

# Class of different styles
class style():
    """
    Class of fifferent styles
    Creds for solution:
    https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    """
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.YELLOW + "Hello, World!" +style.RESET)


def hangman_logo():
    """
    Logo for the game. Generated with: https://www.ascii-art-generator.org/
    """
    print(style.CYAN +
    """
     ____  _ _                 _ _     
    |  _ \(_) | ____ _ _ __ __| ( )___ 
    | |_) | | |/ / _` | '__/ _` |// __|
    |  _ <| |   < (_| | | | (_| | \__ /
    |_| \_\_|_|\_\__,_|_|  \__,_| |___/

     _   _                                         
    | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    |  _  | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       

    """
    + style.RESET)
    print(style.RED +
        """
         ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """
        + style.RESET)
    # Welcoming the player to the game
    print("\nWelcome to Rikard's Hangman!\n")
    global name
    name = input("Enter your nickname: \n")
    print("\n")
    print(style.CYAN + f"Good Luck, {name}!" + style.RESET)
    print("\n")
    return name


def get_word():
    """
    Gets a random word from words.txt. 
    List generated from https://www.randomlists.com/random-words
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()


def play(word):
    """
    Plays the game and checks if guessed letters are correct or not
    Credits for inspiration to: https://youtu.be/m4nEnsavl6w
    """
    word_progress = "_" * len(word)
    print(word_progress)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = lives
    while not guessed and tries > 0:
        guess = input("Guess a letter:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have already guesssed {guess}. Try another letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                if tries == 0:
                    # Prints the hangman status
                    print("""
                    ___________
                    |/        |
                    |         O
                    |        /|\\
                    |         |
                    |        / \\
                    |\\
                    ========
                    """)

                if tries == 1:
                    print("""
                    ___________
                    |/        |
                    |         O
                    |        /|\\
                    |         |
                    |        /
                    |\\
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 2:
                    print("""
                    __________
                    |/        |
                    |         O
                    |        /|\\
                    |         |
                    |
                    |\\
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 3:
                    print("""
                    __________
                    |/        |
                    |         O
                    |        /|
                    |         |
                    |
                    |\\
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 4:
                    print("""
                    __________
                    |/        |
                    |         O
                    |         |
                    |         |
                    |
                    |\\
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 5:
                    print("""
                    __________
                    |/        |
                    |         O
                    |
                    |
                    |
                    |\\
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 6:
                    print("""
                    __________
                    |/
                    |
                    |
                    |
                    |
                    |\\
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 7:
                    print("""
                    __________
                    |/
                    |
                    |
                    |
                    |
                    |
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 8:
                    print("""
                    |/
                    |
                    |
                    |
                    |
                    |
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 9:
                    print("""
                    |
                    |
                    |
                    |
                    |
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 10:
                    print("""
                    |
                    |
                    |
                    |
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 11:
                    print("""
                    |
                    |
                    |
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")

                if tries == 12:
                    print("""
                    |
                    ========
                    """)
                    print(f"You have {tries} live(s) left.")                                            

                guessed_letters.append(guess)
            else:
                print(f"Nicely done! {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_progress)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_progress = "" .join(word_as_list)
                if "_" not in word_progress:
                    guessed = True                                      
        else:
            print(style.YELLOW + "Not a valid guess. Try again." + style.RESET)
        print(word_progress)
        print("\n")                        
    if guessed:
        print(style.GREEN + f"You guessed the word! You win, {name}!" + style.RESET)
    else:
        print(style.RED + f"Sorry {name}, you lost... The word was: {word}." + style.RESET)    


def show_rules():
    print(
        """
        Choose a letter from A to Z.\n
        If it's not in the word, you loose a life.\n
        If it's correct it will show in the word.\n
        The game is over if you loose all lives.\n
        You win if you get all letters right!
        \n
        """
        + style.CYAN + f"Good luck, {name}!"
        + style.RESET)
    input(style.YELLOW + "Press enter to return to menu" + style.RESET)
    menu()


def menu():
    """
    Presents choices to the player
    """
    print("Press 1 to start the game")
    print("Press 2 to show the rules \n")
    choice = input("Enter number: \n")
    global lives
    lives = 0
    if choice == "2":
        show_rules()
    elif choice == "1":
        print(style.GREEN + "Easy = 12 lives" + style.RESET)
        print(style.CYAN + "Medium = 8 lives" + style.RESET)
        print(style.RED + "Hard = 6 lives\n" + style.RESET)
        level = False
        while not level:
            level = input(
                "Press E for Easy, M for Medium or H for Hard: "
                ).upper()
            if level == "E": 
                level = True
                lives = 12
                return lives
            elif level == "M":
                level = True
                lives = 8
                return lives
            elif level == "H":
                level = True
                lives = 6
                return lives
            else:
                print("Please choose E, M or H")
                level = False
    else:
        print(style.YELLOW + 'Please choose 1 or 2.' + style.RESET)
        menu()


def main():
    """
    Runs the game
    """          
    hangman_logo()
    word = get_word()
    menu()
    play(word)
    while input(style.YELLOW + "Start over? (Y/N)" + style.RESET).upper() == "Y":
        word = get_word()
        play(word)
    else:
        main()    


main()


