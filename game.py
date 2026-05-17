from words import words
from utils import hangman_stages
from score_manager import save_score, display_high_scores

import random


class HangmanGame:

    def __init__(self):

        self.selected_category = ""
        self.selected_difficulty = ""

        self.word = ""

        self.guessed_letters = []

        self.wrong_guesses = 0
        self.max_wrong_guesses = 6

        self.score = 0

    def choose_category(self):

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

                self.selected_category = categories[choice - 1]
                return

            print("Invalid choice. Try again.")

    def choose_difficulty(self):

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

                self.selected_difficulty = difficulties[choice - 1]
                return

            print("Invalid choice. Try again.")

    def select_word(self):

        self.word = random.choice(
            words[self.selected_category][self.selected_difficulty]
        )

    def display_progress(self):

        print(hangman_stages[self.wrong_guesses])

        display_word = ""

        for letter in self.word:

            if letter in self.guessed_letters:
                display_word += letter + " "

            else:
                display_word += "_ "

        print(display_word)

        print(f"\nCurrent Score: {self.score}")

        return display_word

    def process_guess(self):

        guess = input("\nEnter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():

            print("Please enter a single alphabet letter.")
            return

        if guess in self.guessed_letters:

            print("You already guessed that letter.")
            return

        self.guessed_letters.append(guess)

        if guess in self.word:

            self.score += 10

            print("\nCorrect Guess! +10 Points")

        else:

            self.wrong_guesses += 1

            print("\nIncorrect Guess!")

            print(
                f"Remaining Lives: "
                f"{self.max_wrong_guesses - self.wrong_guesses}"
            )

    def save_player_score(self):

        player_name = input("\nEnter your name: ")

        save_score(player_name, self.score)

        display_high_scores()

    def start(self):

        self.choose_category()

        self.choose_difficulty()

        self.select_word()

        print(f"\nCategory: {self.selected_category}")

        print(f"Difficulty: {self.selected_difficulty}")

        print("\nWelcome to Hangman!\n")

        while self.wrong_guesses < self.max_wrong_guesses:

            display_word = self.display_progress()

            if "_" not in display_word:

                self.score += 50

                print("\nYou Won!")

                print("Bonus Awarded: +50")

                print(f"\nFinal Score: {self.score}")

                self.save_player_score()

                return

            self.process_guess()

        print(f"\nGame Over! The word was: {self.word}")

        print(f"\nFinal Score: {self.score}")

        self.save_player_score()