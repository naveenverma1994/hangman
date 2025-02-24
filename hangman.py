import random
# List of hang
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
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
 /|   |
      |
      |
=========''', '''
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
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
               
# List of words to choose from
words_list = ['pytohon', 'java', 'kotllin', 'javascript']
# Randomly select a word from the list
word = random.choice(words_list)
# Create a list of underscores with length equal to the word
blank_list = list('_' * len(word))
print(blank_list)
# Get initial guess from user
guess = input("Guess the characters:")
# Initialize lives
lives = 7

# Main game loop
while lives > 0:
  # Check if guessed character is in the word
  if guess in word:
    # Replace underscore with correctly guessed character
    for i in range(len(word)):
      if word[i] == guess:
        blank_list[i] = guess
    print(blank_list)
    print("You Survived! Lives left:", lives, HANGMANPICS[lives])
    guess = input("Guess another word:")
      
  else:
    # Reduce lives for incorrect guess
    lives -= 1
    print("You Loose! Lives left:", lives, HANGMANPICS[lives])
    guess = input("Guess again:")
    continue

# Game over messages
print("You Loose! The word was:", word)
print(HANGMANPICS[lives])
print("Game Over!")