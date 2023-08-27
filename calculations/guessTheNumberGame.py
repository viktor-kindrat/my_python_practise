import random

def check_if_win (random_number, user_variant):
    if random_number == user_variant:
        return True
    else: 
        return False

def get_hint (user_prompt, guessed_numer):
    if user_prompt > guessed_numer: 
        return("Guessed number is less than you prompted")
    else: 
        return("Guessed number is more than you prompted")


def setup_game (from_num, to_num):
    user_win = False
    guessed_numer = random.randint(from_num, to_num)
    while not user_win: 
        try: 
            user_prompt = int(input("Guess the number from " + str(from_num) + " to " + str(to_num) + ": "))
        except ValueError: 
            print("\U0001F914 Enter an integer number!")
            continue
        
        user_win = check_if_win(guessed_numer, user_prompt)
        if user_win: 
            print("\U0001F947 Congratulations! You win!")
        else: 
            print("\u274C No it is not \"" + str(user_prompt) + ". Try again (Hint: " + get_hint(int(user_prompt), guessed_numer) + ")")

setup_game(0, 100)