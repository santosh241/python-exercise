# a = [1, 2, 3, 4, 5]
# print(a)
# for i in range(0, len(a)):
#    print(a[i])
# print(" in reverse order: ")
# for i in range(len(a)-1,-1,-1):
#    print(a[i], end="")

#############################################
# import random
# num = random.randint(1, 100)
# while True:
#    print('Guess a number between 1 and 100')
#    guess = input()
#    i = int(guess)
#    if i == num:
#        print('You won!!!')
#        break
#    elif i < num:
#         print('Try Higher')
#    elif i > num:
#        print('Try Lower')
# print('if you gussed less than 6 times you won')

# This is a guess the number game.
import random

guessesTaken = 0
print('Hello! What is your name?')
myName = input()
number = random.randint(1, 100)
print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')
while guessesTaken < 6:
    print('Take a guess.')
    guess = int(input())
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    elif guess == number:
        print("you won!!!!")
        print(guessesTaken, "you took guesses")
        break
    print(6-guessesTaken," left chances")


    # elif guess == number:
    #     guessesTaken = str(guessesTaken)
    #     print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    # elif guess != number:
    #     number = str(number)
    #     print('Nope. The number I was thinking of was ' + number)