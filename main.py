import random

import random

letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
               '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~']


# Function to check and append correct letter for "Hello"
def check_and_add_letter(target_letter, letter_list):
    while True:
        letter = random.choice(letter_list)
        if letter == target_letter:
            return letter
        else:
            continue



def generate_hello():
    string = ""
    string += check_and_add_letter("H", letters_upper)
    string += check_and_add_letter("e", letters_lower)
    string += check_and_add_letter("l", letters_lower)
    string += check_and_add_letter("l", letters_lower)
    string += check_and_add_letter("o", letters_lower)

    return string

def generate_world():
    string = " "
    string += check_and_add_letter("W", letters_upper)
    string += check_and_add_letter("o", letters_lower)
    string += check_and_add_letter("r", letters_lower)
    string += check_and_add_letter("l", letters_lower)
    string += check_and_add_letter("d", letters_lower)


    string += check_and_add_letter("!", punctuation)

    return string



string = generate_hello() + generate_world()


print(string)



