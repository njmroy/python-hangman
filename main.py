# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import time

# Initial steps to start game
print("\nWelcome to the Hangman Game!")
name = input("Enter your name: ")
print("Hello " + name + "! Good luck.")
time.sleep(2)
print("The game is starting now.")
time.sleep(2)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "swamp", "answer", "justice", "wisteria"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    # line of letters size of word to display
    display = '_' * length
    # List to contain string index of correct words
    already_guessed = []
    play_game = ""


def play_loop_start():
    return input("Do you want to play again? y = yes, n = no")


def play_loop():
    while play_loop_start() not in ["y", "Y", "n", "N"]:
        play_game = play_loop_start()
        if play_game == "y":
            main()
        elif play_game == "n":
            print("Thanks for playing! Bye!")
            exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the hangman word: " + display + " Enter your guess: \n")
    guess = guess.strip()

    # Check for no input, 2 letters at once, or num
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid prompt, try a letter!\n")
        hangman()
    elif guess in word:

