import random

num = random.randint(1,10)

print('You have 3 tries to guess my number')
tries = 2
print('Please enter an integer number between 1 and 10')
guess = int(input('Input your guess: '))
play = True
while tries > 0:
    if guess != num:
        tries -= 1
        if guess > num:
            print('Lower')
        else:
            print('Higher')
        guess = int(input('Input your guess: '))
    elif num == guess:
        print('Hooray')
        tries = 0

if (num != guess) and (tries == 0):
    print('Sorry you lose')