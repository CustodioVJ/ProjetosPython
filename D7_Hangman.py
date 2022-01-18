import random

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

#randomly choose a word for our game:
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#defining conditions for the game
display = []
lives = 6
letter = ""

for u in range(len(chosen_word)):
    display += "_"
print(display, "\n")


#checking the gamer answer and if he's not out of lives:
while display[0 -1] == "_" and lives != 0:
    guess = input("Please, guess a letter: ").lower()

    for l in range(len(chosen_word)):
        le = chosen_word[l]
        if guess == le:
            display[l] = le
    print(display, "\n")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            letter = "Fail"
    print(stages[lives])

for l in display:
    letter += l

if letter == chosen_word:
    print("You won")
else:
    print("You lose")










