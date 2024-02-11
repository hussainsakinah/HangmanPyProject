import random
import Hangman_wordlist
import Hangman_art
print(Hangman_art.logo)
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
word_list = Hangman_wordlist.word_list
chosen_word = random.choice(word_list)
print(f"Shhhh....The chosen word is {chosen_word}")


word_length = len(chosen_word)
display = []
lives = 6
for letter in chosen_word:
    display.append("_")

while "_" in display and lives > 0:
    guess = input("Enter your guessed letter: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            if guess in display:
                print("You chose this letter")
    if guess not in chosen_word:
        print("Letter isn't in the word")
        print(stages[lives-1])
        lives-=1
    if lives == 0:
        print("You Lose")

    print(display)
    word_length -= 1
if "_" not in display:
    print("You win!")



