import random

# Step 1: word list
words = ["movie", "actor", "direction", "production", "cinema", "screenplay", "soundtrack", "stunt", "costume"];

# Step 2: choose random word
word = random.choice(words)

# Step 3: create blanks
guessed = ["_"] * len(word)

lives = 6
used_letters = []

print("Welcome to Hangman!")

# Step 4: game loop
while lives > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Lives left:", lives)
    print("Used letters:", used_letters)

    guess = input("Enter a letter: ").lower()

    # avoid repeated guess
    if guess in used_letters:
        print("Already guessed!")
        continue

    used_letters.append(guess)

    # check if correct
    if guess in word:
        print("Correct!")

        # fill letters
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong!")
        lives -= 1

# Step 5: result
if "_" not in guessed:
    print("\n🎉 You won! Word was:", word)
else:
    print("\n💀 You lost! Word was:", word)