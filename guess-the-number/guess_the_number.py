import random

def is_valid_num(s):
    if s.isdigit() and 1 <= int(s) <= 100:
        return True
    else:
        return False

def main():
    number = random.randint(1,100)
    guess = input("Guess a number between 1 and 100: ")
    guessed_number = False
    num_guesses = 0
    while not guessed_number:
        if not is_valid_num(guess):
            guess = input("I won't count that one. A number is between 1 and 100. Guess again: ")
            continue
        else:
            num_guesses +=1
            guess = int(guess)
        
        if guess < number:
            guess = input("Too low guess again: ")
        elif guess > number:
            guess = input("Too high guess again: ")
        else:
            print("You got it in ",num_guesses," guesses!")
            guessed_number = True
main()
