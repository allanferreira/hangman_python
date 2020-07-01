def main():
    lifes = 6
    win = None
    secret_word = "banana"
    display_letters = list("_" * len(secret_word))

    print("* Welcome to The Hangman")
    while win is None:
        print("=======================")
        print(f"Lifes: {lifes}")
        print(" ".join(display_letters))
        print("=======================")
        guess = input("Guess a letter: ")

        if guess in secret_word:
            print("Good!")
            for i, letter in enumerate(secret_word):
                if letter is guess:
                    display_letters[i] = guess

        else:
            print("Bad...")
            lifes -= 1

        if '_' not in display_letters:
            win = True
        elif lifes == 0:
            win = False

    print("=======================")
    print(f"Lifes: {lifes}")
    print(" ".join(display_letters))
    print("=======================")
    
    if win:
        print("Congratulations! You won.")
    else:
        print(f"What a shame! The word is '{secret_word}'")

    print("Thanks for playing")


if __name__ == "__main__":
    main()
