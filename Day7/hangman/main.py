# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)
display_word = []
for index in range(0, len(word)):
    display_word.append("_")
print(display_word)

end_of_game = False
while not end_of_game:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ")

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    # for letter in word:
    #     if guess == letter:
    #         print("Right")
    #     else:
    #         print("Wrong")

    # TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    for index in range(0, len(word)):
        if guess == word[index]:
            display_word[index] = guess
    print(display_word)
    if "_" not in display_word:
        end_of_game = True
print("You won.")

