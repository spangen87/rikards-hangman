import random


def hangman_logo():
    """
    Logo for the game. Generated with: https://www.ascii-art-generator.org/
    """
    print(
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
    )
    # Welcoming the player to the game
    print("\nWelcome to Rikard's Hangman!")
    global name
    name = input("Enter your nickname: \n")
    print("\n")
    print(f"Good Luck, {name}!")
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
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed {guess}")
            elif guess != word:
                print(f"{guess} is not the correct word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_progress = word                       
        else:
            print("Not a valid guess. Try again.")
        print(word_progress)
        print("\n")                        
    if guessed:
        print(f"You guessed the word! You win, {name}!")
    else:
        print(f"Sorry {name}, you lost... The word was: {word}.")    


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
        f"Good luck, {name}!"
        )
    input("Press enter to return to menu")
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
        print("Easy = 12 lives")
        print("Medium = 8 lives")
        print("Hard = 6 lives\n")
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
        print('Please choose 1 or 2.')
        menu()


def main():
    """
    Runs the game
    """          
    hangman_logo()
    word = get_word()
    menu()
    play(word)
    while input("Start over? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)
    else:
        main()    


main()


