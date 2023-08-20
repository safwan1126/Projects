import random
import sys

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

word = word_list[random.randint(0, len(word_list) - 1)]

empty = []
stage = 0
correct = False
for i in range(0, len(word)):
    empty += '_'
while '_' in empty:
    if stage == len(stages):
        print(f'You Lose, Correct word was {word}')
        sys.exit()
    guess = input(f'Guess a letter: {empty}\n').lower()
    correct = False
    if guess in empty:
        print('You already guessed that')
    for i in range(len(word)):
        if guess == word[i]:
            empty[i] = guess
            correct = True
    if not correct:
        stage += 1
        print('Wrong letter\n' + stages[len(stages) - stage])

if '_' not in empty:
    print('You Win')
