############This is a Word Guessing Game project

import random

# List of words for the game
words = ["python", "java", "javascript", "ruby", "cplusplus", "programming"]

def choose_word():
    # Choose a random word from the list
    return random.choice(words)

def play_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts allowed

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word. You have", attempts, "attempts.")

    while attempts > 0:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print("Word:", display_word)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if "_" in display_word:
        print("Out of attempts. The word was:", word_to_guess)

play_game()
