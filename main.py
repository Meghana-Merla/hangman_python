from game import start_game


while True:

    start_game()

    while True:

        choice = input("\nDo you want to play again? (Y/N): ").lower()

        if choice == "y":
            break

        elif choice == "n":
            print("\nThanks for playing Hangman!")
            exit()

        else:
            print("Please enter Y or N.")