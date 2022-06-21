import random

def get_word():
    """
    Gets a random word from words.txt
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    print(random_word.upper())

get_word()

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
               
