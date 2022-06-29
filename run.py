import random
import os


# System call
os.system("")


class Style():
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


def hangman_logo():
    """
    Logo for the game. Generated with: https://www.ascii-art-generator.org/
    """
    print(Style.BLUE + """
        ____  _ _                 _ _
        |  _ \(_) | ____ _ _ __ __| ( )___
        | |_) | | |/ / _` | '__/ _` |// __|
        |  _ <| |   < (_| | | | (_| | \__ /
        |_| \_\_|_|\_\__,_|_|  \__,_| |___/

         _   _
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
        | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
        |  _  | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            |___/
    """ + Style.RESET)

    # Welcoming the player to the game
    print("\nWelcome to Rikard's Hangman!\n")
    global name
    while True:
        name = input("Enter your name? ")
        if name.isalpha():
            break
        print(Style.YELLOW + "You can only use letters in name!" + Style.RESET)
    print("\n")
    print(Style.CYAN + f"Good Luck, {name}!" + Style.RESET)
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
    Credits to: https://youtu.be/m4nEnsavl6w
    """
    word_progress = "-" * len(word)
    print(f"The word has {len(word)} letters.")
    print(word_progress)
    guessed = False
    guessed_letters = []
    tries = lives
    while not guessed and tries > 0:
        print(f"Already guessed: {guessed_letters}")
        guess = input("Guess a letter:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(
                    Style.YELLOW + f"""
You have already guesssed {guess}. Try another letter.
                    """ + Style.RESET)
            elif guess not in word:
                print(Style.RED + f"{guess} is not in the word." + Style.RESET)
                tries -= 1
                if tries == 0:
                    # Prints the hangman status
                    print(Style.RED + """
                    ___________
                    |/        |
                    |         O
                    |        /|\\
                    |         |
                    |        / \\
                    |\\
                    ========
                    """ + Style.RESET)

                if tries == 1:
                    print(Style.RED + """
                    ___________
                    |/        |
                    |         O
                    |        /|\\
                    |         |
                    |        /
                    |\\
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 2:
                    print(Style.RED + """
                    __________
                    |/        |
                    |         O
                    |        /|\\
                    |         |
                    |
                    |\\
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 3:
                    print(Style.RED + """
                    __________
                    |/        |
                    |         O
                    |        /|
                    |         |
                    |
                    |\\
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 4:
                    print(Style.RED + """
                    __________
                    |/        |
                    |         O
                    |         |
                    |         |
                    |
                    |\\
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 5:
                    print(Style.RED + """
                    __________
                    |/        |
                    |         O
                    |
                    |
                    |
                    |\\
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 6:
                    print(Style.RED + """
                    __________
                    |/
                    |
                    |
                    |
                    |
                    |\\
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 7:
                    print(Style.RED + """
                    __________
                    |/
                    |
                    |
                    |
                    |
                    |
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 8:
                    print(Style.RED + """
                    |/
                    |
                    |
                    |
                    |
                    |
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 9:
                    print(Style.RED + """
                    |
                    |
                    |
                    |
                    |
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 10:
                    print(Style.RED + """
                    |
                    |
                    |
                    |
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 11:
                    print(Style.RED + """
                    |
                    |
                    |
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                if tries == 12:
                    print(Style.RED + """
                    |
                    ========
                    """ + Style.RESET)
                    print(f"You have {tries} live(s) left.")

                guessed_letters.append(guess)
            else:
                print(Style.GREEN + f"""
Nicely done! {guess} is in the word!
                """ + Style.RESET)
                guessed_letters.append(guess)
                word_as_list = list(word_progress)
                indices = [
                    i for i, letter in enumerate(word) if letter == guess
                    ]
                for index in indices:
                    word_as_list[index] = guess
                word_progress = "" .join(word_as_list)
                if "-" not in word_progress:
                    guessed = True
        else:
            print(Style.YELLOW + "Not a valid guess. Try again." + Style.RESET)
        print(word_progress)
        print("\n")
    if guessed:
        print(Style.GREEN + """
        __  __               _       ___       __
        \ \/ /___  __  __   | |     / (_)___  / /
        \  / __ \/ / / /   | | /| / / / __ \/ /
        / / /_/ / /_/ /    | |/ |/ / / / / /_/
        /_/\____/\__,_/     |__/|__/_/_/ /_(_)
        """ + Style.RESET)
        print(Style.GREEN + f"""
You guessed the word! You win, {name}!
        """ + Style.RESET)
    else:
        print(Style.RED + """
        __  __               __                    __
        \ \/ /___  __  __   / /   ____  ________  / /
        \  / __ \/ / / /  / /   / __ \/ ___/ _ \/ /
        / / /_/ / /_/ /  / /___/ /_/ (__  )  __/_/
        /_/\____/\__,_/  /_____/\____/____/\___(_)
        """ + Style.RESET)
        print(Style.RED + f"""
Sorry {name}, you lost... The word was: {word}.
        """ + Style.RESET)


def show_rules():
    """
    Showing the rules for the game
    """
    print(
        """
    Choose a letter from A to Z.\n
    If it's not in the word, you loose a life.\n
    If it's correct it will show in the word.\n
    The game is over if you loose all lives.\n
    You win if you get all letters right!
    \n
        """)
    print(Style.CYAN + f"Enjoy the game, {name}!" + Style.RESET)
    input(Style.YELLOW + "Press ENTER to return to menu.\n" + Style.RESET)
    menu()


def menu():
    """
    Presents choices to see the rules or choosing level
    """
    print("Press 1 to start the game")
    print("Press 2 to show the rules \n")
    choice = input(Style.YELLOW + "Enter number: \n" + Style.RESET)
    global lives
    lives = 0
    if choice == "2":
        show_rules()
    elif choice == "1":
        print(Style.GREEN + "Easy = 12 lives" + Style.RESET)
        print(Style.CYAN + "Medium = 8 lives" + Style.RESET)
        print(Style.RED + "Hard = 6 lives\n" + Style.RESET)
        level = False
        while not level:
            level = input(Style.YELLOW + """
Press E for Easy, M for Medium or H for Hard:
            """ + Style.RESET).upper()
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
                print(Style.YELLOW + "Please choose E, M or H" + Style.RESET)
                level = False
    else:
        print(Style.YELLOW + "Please choose 1 or 2." + Style.RESET)
        menu()


def main():
    """
    Runs the game
    """
    hangman_logo()
    word = get_word()
    menu()
    play(word)

    # Give the option to replay
    while input(
        Style.YELLOW + "Start over? (Y/N)" + Style.RESET
                ).upper() == "Y":
        word = get_word()
        menu()
        play(word)
    else:
        main()


main()
