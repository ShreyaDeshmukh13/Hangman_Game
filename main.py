import random
from Tools.scripts.dutree import display
stages=[
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
    '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
   =========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''u
  +---+
  |   |
      |
      |
      |
      |
========='''
]
from wordbank import word_list
lives=6
chosen_word=random.choice(word_list)
print("GAME STARTED")
print("Guess the letters of the word")
#print(chosen_word)

word_length=len(chosen_word)
placeholder= ""
for position in range(word_length):
    placeholder+="_"
print(placeholder)

game_over=False
correct_letters=[]

while not game_over:
    guess=input("Guess a letter : ").lower()
  #  print(guess)

    display=""
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display+="_"

    print(display)

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose.")
            print(f"The word was {chosen_word}")
    if "_" not in display:
        game_over=True
        print("You win!")

    print(stages[lives])