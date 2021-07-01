import sys, os
import random, time

def clear_window(t):
    time.sleep(t)
    try:
        os.system('cls')
    except:
        os.system('clear')



def game():
    print('Hello, Welcome to Guessing the Number Game!\n You get 3 chances to guess the number. Are you ready to play?')
    choice = input("Press Y to start the game or N to quit.").lower()

    if choice=='y':
        clear_window(0)
        play()
    elif choice=='n':
        clear_window(0)
        sys.exit()
    else:
        game()
    loop=False


def play():
    for i in range(3):
        name = input('Enter your name: ')
        print("Guess a number between 0 to 10\n")
        try:
            guess = int(input('Enter your guess: '))
        except :
            try:
                guess = int(input('The entered number is invalid. Please enter your number again'))
            except :
                print('Sorry, Invalid number.')
                clear_window(3)
                game()
        random_number = random.randint(0,10)
        while guess != random_number:
            print('Sorry, guessed number is incorrect')
            if guess>random_number:
                print("You guessed a higher number.")
                try:
                    guess = int(input('\nTake another guess: '))
                except :
                    try:
                        guess = int(input('Invalid guess, please try again'))
                    except:
                        print('Sorry, Invalid number.')
                        clear_window(3)
                        game()
            if  guess<random_number:
                print('You guessed a lower number.')
                try:
                    guess = int(input('\nTake another guess: '))
                except :
                    try:
                        guess = int(input('Invalid guess, please try again'))
                    except:
                        print('Sorry, Invalid number.')
                        clear_window(3)
                        game()


    print('Congratulations {}!! You guessed it right.'.format(name))
    print('Returning to the main menu.....')
    print('*************************************************\n')
    clear_window(3)
    game()

def main():
    game()


if __name__ == '__main__':
    main()