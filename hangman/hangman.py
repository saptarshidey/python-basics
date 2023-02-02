import random
from words import words
from visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()  # what the user has guessed
    lives = 7

    # get user input
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left and you have used these letters: {','.join(guessed_letters)}")

        # what current word is (i.e W - R D)
        deciphered_word = [letter if letter in guessed_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print(f"Current word: {' '.join(deciphered_word)}")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1  # takes away a life if wrong
                print(f"Your letter, {user_letter}, is not in the word")

        elif user_letter in guessed_letters:
            print("You have already used that letter. Guess another letter")

        else:
            print("That is not a valid letter")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"You died, sorry. The word was {word}")
    else:
        print(f"YAY! You guessed the word, {word}")


if __name__ == '__main__':
    hangman()
