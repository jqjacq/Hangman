from random import choice


def word_selection():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()


print(word_selection())
