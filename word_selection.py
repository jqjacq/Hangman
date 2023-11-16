from random import choice
# Select random word from words.txt
def word_selection():
    with open("words.txt", "r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()
