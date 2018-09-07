import random

letters = 'abcdefghijklmnopqrstuvwxyz'
letter = letters[random.randint(0,25)]

while True:
    guess = input('Type a lower-case letter:   ')
    if guess not in letters:
        print('That is not a lower-case letter:   ')
        continue
    if guess == letter:
        print('You won!')
        break
    if guess > letter:
        print('It is earlier in the alphabet')
    else:
        print('It is later in the alphabet')



