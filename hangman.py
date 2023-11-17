from draw_hangman import draw_hangman as draw_hangman #Draws the hangman
from word_selection import word_selection as hidden_word #Selects a random word from words.txt
from users_input import get_user_input as user_input #Gets user input

max_incorrect_guesses = 6

# Display the word with underscores for letters not yet guessed
def display_word(word, letters_guessed):
    correct_letters = ''
    for letter in word:
        if letter in letters_guessed:
            correct_letters += letter
            # correct_letters.append(letter)
        else:
            correct_letters += "_ "
            # correct_letters.append("_")
    return correct_letters
            #" ".join(correct_letters)

# Display the letters that have been guessed
def join_letters_guessed(letters_guessed):
    return " ".join(sorted(letters_guessed))

# Display the progress
def display_progress(hidden_word, letters_guessed, remaining_guesses):
    word_progress = ''.join(letter if letter in letters_guessed else "_" for letter in hidden_word)

    print(f"Word to guess: {word_progress}")
    print(f"Letters guessed: {join_letters_guessed(letters_guessed)}")
    print(f"Remaining lives: {remaining_guesses}")


# Start and loop through the game
def hangman(hidden_word):
    remaining_guesses = max_incorrect_guesses
    letters_guessed = []

    while remaining_guesses > 0:
        display_progress(hidden_word, letters_guessed, remaining_guesses) #display progress
        draw_hangman(6 - remaining_guesses) #display hangman
        guess = user_input(letters_guessed) #get user input
        letters_guessed.append(guess)
        if guess in hidden_word:
            print("Correct!")
        else:
            print("Incorrect!")
            remaining_guesses -= 1

        if remaining_guesses == 0:
            draw_hangman(max_incorrect_guesses - remaining_guesses)
            print("You ran out of tries! The word was " + hidden_word + ".")
        
        # Check if all letters have been guessed
        if "_" not in display_word(hidden_word, letters_guessed):
            print("Congratulations! You guessed the word!")
            break

    play_again()

# Ask if the user wants to play again
def play_again():
    while True:
        play_again = input("Do you want to play again? (Y/N) ").lower()
        if play_again == "y":
            hangman(hidden_word())
        elif play_again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter Y or N.")

# Start the game
hangman(hidden_word())