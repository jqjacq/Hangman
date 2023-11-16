import string

# Validate user input
def validate_input(user_input, letters_guessed):
    return (
        len(user_input) == 1
        and user_input in string.ascii_lowercase
        and user_input not in letters_guessed
    )

# Get user input
def get_user_input(letters_guessed):
    while True:
        user_input = input("Guess a letter: ").lower()
        if validate_input(user_input, letters_guessed):
            return user_input
        elif user_input in letters_guessed: #Check if letter has already been guessed
            print("You already guessed that letter. Please try a different letter.")
        else:
            print("Invalid input. Please try again and enter a single letter.")
