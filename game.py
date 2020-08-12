import random

num = random.randint(1, 100)

def user_guess():
    guess = input("Guess a number between 1 and 100: ")
    print("Your guess is", guess)
    guess = int(guess)

    while guess != num:
        if guess < num:
            guess = input("Your guess was too low: guess again!")
            print("Your guess is", guess)
            guess = int(guess)
        if guess > num:
            guess = input("Your guess was too high: guess again!")
            print("Your guess is", guess)
            guess = int(guess)
        if guess == num:
            print("Correct! Well done!")
            again = input("Would you like to play again? (Y or N): ")
            if again == "y":
                user_guess()
            break

user_guess()