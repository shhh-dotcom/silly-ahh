# P.16 for game explanation.
import random
from colorama import Style, Fore

w = 'welcome to Stars and Moons!\n'.center(145)
a = '1. Instructions\n'.center(25)
b = '2. Start Game\n'.center(132)
c = '3. Exit'.center(17)
menu = w + a + b + c

def bro_plays():
    moons = 0
    stars = 0
    randomnum = random.sample(range(1, 21), 4)
    save = randomnum.copy()
    tries = 4

    while tries > 0:
        randomnum2 = []
        try:
            guess = input('Enter your guess (separate each number with a space): ').split()
            guess = [int(item) for item in guess]
            if len(guess) != 4:
                print(Fore.RED + "Please enter exactly 4 numbers!" + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.RED + "Invalid input. Enter numbers only!" + Style.RESET_ALL)
            continue

        tries -= 1
        for i, (a, b) in enumerate(zip(randomnum, guess)):
            if a == b:
                print(Fore.CYAN + f'{a} and {b} match at index {i}' + Style.RESET_ALL)
                print(Fore.GREEN + 'You get 1 star, keep guessing..' + Style.RESET_ALL)
                stars += 1
            elif a in guess:
                print(Fore.LIGHTBLACK_EX + f'{a} is correct but in the wrong position, you get 1 moon' + Style.RESET_ALL)
                moons += 1
            else:
                randomnum2.append(a)

        if tries > 0:
            print(Fore.BLUE + f'Keep guessing! You have {tries} tries left.' + Style.RESET_ALL)

        randomnum = randomnum2
        if not randomnum:

            print(Fore.LIGHTGREEN_EX + 'You won!!' + Style.RESET_ALL)
            print(Fore.BLACK + f'The mysterious number was {save}' + Style.RESET_ALL)
            break

    print(Fore.YELLOW + f'You obtained {moons} moons and {stars} stars' + Style.RESET_ALL)
    if tries == 0 and randomnum:
        print(Fore.RED + 'You are out of attempts. You lose.' + Style.RESET_ALL)
        print(Fore.BLACK + f'The mysterious number was {save}' + Style.RESET_ALL)

    a = input('Do you want to return to the menu? (yes/no): ').lower()
    if a == 'yes':
        print(menu)
    else:
        print('Farewell!')

def main():
    global o  # Declaring 'o' as a global variable
    print(Fore.GREEN + menu + Style.RESET_ALL)

    while True:
        try:
            o = int(input(Fore.RED + 'Please choose an option: '.rjust(85) + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Invalid input! Enter a number." + Style.RESET_ALL)
            continue

        if o == 1:
            print(Fore.BLUE + "Game Instructions:\n"
                  "1 - You receive a **Star** for each correct digit in the correct position.\n"
                  "2 - You receive a **Moon** for each correct digit in the wrong position.\n"
                  "3 - If none are correct, you receive nothing.\n"
                  "4 - You have **4 guesses** total.\n"
                  "5 - If you run out of guesses, you **lose**.\n"
                  "Simple enough? Good luck!" + Style.RESET_ALL)
            print(menu)
        elif o == 2:
            bro_plays()
        elif o == 3:
            print('Goodbye!')
            break
        elif o == 69:
            print('Looking for an Easter egg? Take your reward and go.')
        else:
            print(Fore.RED + 'Invalid option! Please select 1, 2, or 3.' + Style.RESET_ALL)
            print(menu)

# Flask-compatible function
def some_function():
    return "This is from project_or_smth!"

# Run the game in standalone mode
if __name__ == "__main__":
    main()

# well that was a ride..

#so is that it?..
#these some schizo comments from before:
# changed a LOT of shit on the 3rd task P.76 basically rewrote this whole ass project
# Task.1 P.45:

# Task.2 P.59
# greendale cc ahh introduction

 # bruh this looks nothing like the original
    




        



# Done for now...
# pretty good for now
# ayy bruh  I just came back



