from words import words
import random


def start_game():

    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\nWelcome to Hangman!\n")

    while wrong_guesses < max_wrong_guesses:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word)

        if "_" not in display_word:
            print("\nYou Won!")
            break

        guess = input("\nEnter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        # Duplicate guess check
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1
            print(f"Wrong Guess! Remaining Lives: {max_wrong_guesses - wrong_guesses}")

    else:
        print(f"\nGame Over! The word was: {word}")