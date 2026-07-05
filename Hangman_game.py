import random

words = ["python", "computer", "science", "coding", "program"]

secret_word = random.choice(words)

guessed_letters = []
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts Left:", attempts)

    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # If-else condition
    if guess in secret_word:
        print(" Correct Guess!")
    else:
        print("Wrong Guess!")
        attempts -= 1

if attempts == 0:
    print("\n Game Over!")
    print("The correct word was:", secret_word)