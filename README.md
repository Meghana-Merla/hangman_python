# Hangman Game

A classic Hangman word-guessing game implemented in Python.

## Description

This is a simple command-line Hangman game where the player tries to guess a hidden word by guessing letters one at a time. You have 6 lives (wrong guesses) to figure out the word before losing the game.

## How to Play

1. Run the game with `python hangman.py`
2. A random word will be hidden, displayed as underscores
3. Guess one letter at a time
4. If the letter is in the word, it will be revealed in all positions
5. If the letter is not in the word, you lose one life
6. Win by guessing all letters before losing all 6 lives
7. The game prevents duplicate letter guesses

## Features

- Random word selection
- Real-time word progress display
- Tracks used letters
- Lives counter
- Duplicate guess detection
- Win/lose conditions

## Requirements

- Python 3.x

## Usage

```bash
python hangman.py
```

Then follow the on-screen prompts to play the game!
