from words import words
import random


def choose_category():

    print("\nChoose a Category:\n")

    categories = list(words.keys())

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:

        choice = input("\nEnter your choice: ")

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(categories):
            return categories[choice - 1]

        print("Invalid choice. Try again.")


def choose_difficulty():

    difficulties = ["Easy", "Medium", "Hard"]

    print("\nChoose Difficulty:\n")

    for index, difficulty in enumerate(difficulties, start=1):
        print(f"{index}. {difficulty}")

    while True:

        choice = input("\nEnter your choice: ")

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(difficulties):
            return difficulties[choice - 1]

        print("Invalid choice. Try again.")


def start_game():

    selected_category = choose_category()

    selected_difficulty = choose_difficulty()

    word = random.choice(
        words[selected_category][selected_difficulty]
    )

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print(f"\nCategory: {selected_category}")
    print(f"Difficulty: {selected_difficulty}")

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