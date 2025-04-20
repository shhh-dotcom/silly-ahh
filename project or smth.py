# P.16 for game explanation.
import random
from colorama import Style, Fore

w ='welcome to Stars and Moons!\n'.center(145)
a = '1.Instructions\n'.center(25)
b = '2.Start Game\n'.center(132)
c = '3.Exit'.center(17) 
menu = w + a + b + c
print(Fore.GREEN +menu + Style.RESET_ALL )
o = int((input(Fore.RED +'please choose an option: '.rjust(85) + Style.RESET_ALL)))

def bro_plays():
    moons = 0
    stars = 0
    randomnum = random.sample(range(1, 21), 4)
    save = randomnum

    tries = 4
    while tries > 0:
        randomnum2 = []
        guess = (input('Enter your guess(add space after each number): ')).split()
        guess = [int(item) for item in guess]
        tries -= 1

        for i,(a, b) in enumerate(zip(randomnum, guess)):
            if a == b:
                print(Fore.CYAN + f'{a} and {b} match at index {i}' + Style.RESET_ALL)
                print(Fore.GREEN + 'you get 1 star,keep guessing..' + Style.RESET_ALL)
                stars += 1

            elif a in guess:
                print(Fore.LIGHTBLACK_EX + f'{a} is correct but not at the same index, you get 1 moon' + Style.RESET_ALL)
                moons += 1
            
            else:
                randomnum2.append(a)
        if tries > 0:
            print(Fore.BLUE + f'keep guessing you have {tries} tries left' + Style.RESET_ALL)


        randomnum = randomnum2
        if not randomnum:
            print(Fore.LIGHTGREEN_EX + 'you won!! atleast that\'s what i think for now..' + Style.RESET_ALL)
            print(Fore.BLACK + f'the mysterious number is {save}'  + Style.RESET_ALL)
            break
            
    print(Fore.YELLOW + f'you obtained {moons} moons and {stars} stars' + Style.RESET_ALL)             
    if tries == 0 and randomnum:
        print(Fore.RED +'you don\'t have any more attempts,you lose' + Style.RESET_ALL)
        print(Fore.BLACK +f'the mysterious number is {save}' +Style.RESET_ALL)
    a = input('do you wish to go back to menu?: ')
    if a == 'yes':
        print(menu)
        

    else:
        print('Farewell')


while True:
    if o == 1:
        print(Fore.BLUE + "so basically this is a guessing game,you'll try to guess "
              "a number consisting of 4 digits between 1 and 20:"
              "\n1-you'll receive a Star for each correct digit you guess in its corresponding index."
              "\n2-you'll receive "
              "a Moon for each correct digit you guess that's in a different index."
              "\n3-if you did Not guess any of the digits correctly you'll receive nothing."
              "\n4-each player is limited to 4 guesses only. "
              "\n5-if the player runs out of guesses before they get the correct list of numbers "
              "they loose."
              "\nsimple enough right? and as for the prize.. "
              "its a huge middle finger and a small patch of cocaine,Good luck!\n" + Style.RESET_ALL)
        print(menu)
        o = int((input(Fore.RED +'please choose an option: '.rjust(85) + Style.RESET_ALL)))
    elif o == 2:
        bro_plays()
        o = int((input(Fore.RED +'please choose an option: '.rjust(85) + Style.RESET_ALL)))
    elif o == 3:
        print('GTF outta he\'e')
        break
    elif o == 69:
        print('brae looking for an easter or smth? take your bone and go')
        print('menu')
        o = int((input(Fore.RED +'please choose an option: '.rjust(85) + Style.RESET_ALL)))
    else:
        print('stop being a moron and play the game correctly\n'.center(145))
        print(menu)
        o = int((input(Fore.RED +'please choose an option: '.rjust(85) + Style.RESET_ALL)))




# well that was a ride..

#so is that it?..
#these some schizo comments from before:
# changed a LOT of shit on the 3rd task P.76 basically rewrote this whole ass project
# Task.1 P.45:

# Task.2 P.59
# greendale cc ahh introduction

    




        



# Done for now...
# pretty good for now
# ayy bruh  I just came back



