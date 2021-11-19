# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# TODO-5: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

import random
from hangman_words import word_list
from hangman_art import logo, stages

# set default end_of_game is False
end_of_game = False
wrong = True

# set the number of lives equals the max index of stages list in hangman_art.py file
lives = len(stages) - 1

# logo
print(logo)

# choose a random word in word_list
word = random.choice(word_list)

# display crosswords
display = []
for position in range(0, len(word)):
    display.append("_")
print(display)

# use while loop to find the letter exists in random word or not
while not end_of_game:
    guess = input("Guess a letter: ")
    for position in range(0, len(word)):
        if guess == word[position]:
            display[position] = guess
            wrong = False
    if wrong:
        lives -= 1
    wrong = True
    print(display)
    print(f"Your lives: {lives}")
    print(stages[lives])
    if "_" not in display or lives == 0:
        end_of_game = True
        if '_' not in display:
            print("You won.")
        else:
            print("You lose.")
print("Correct word: " + word)
