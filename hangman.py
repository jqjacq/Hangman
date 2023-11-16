from draw_hangman import draw_hangman as hangman
from word_selection import word_selection as random_word
import string

max_incorrect_guesses = 6

print(random_word())
hangman(0)

# Get user input
def get_user_input(letters_guessed):
    while True:
        user_input = input("Guess a letter: ").lower()
        if validate_input(user_input, letters_guessed):
            return user_input

# Validate user input
def validate_input(user_input, letters_guessed):
    return (
        len(user_input) == 1
        and user_input in string.ascii_lowercase
        and user_input not in letters_guessed
    )

# Display the word with underscores for letters not yet guessed
def display_word(word, letters_guessed):
    output_letters = []
    for letter in word:
        if letter in letters_guessed:
            output_letters.append(letter)
        else:
            output_letters.append("_")
    return " ".join(output_letters)

# Display the letters that have been guessed
def join_letters_guessed(letters_guessed):
    return " ".join(sorted(letters_guessed))

# Check if the game is over
# def game_over(wrong_guesses, target_word, letters_guessed):
#     return (
#         wrong_guesses == max_incorrect_guesses or set(target_word) <= letters_guessed:
#     ) 