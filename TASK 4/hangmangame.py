import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "developer", "coding", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        current_display = display_word(secret_word, guessed_letters)
        print(f"Current Word: {current_display}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        if current_display == secret_word:
            print("Congratulations! You guessed the word.")
            break

        if attempts == 0:
            print(f"Sorry, you ran out of attempts. The word was {secret_word}.")
            break

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            elif guess in secret_word:
                print("Good guess!")
            else:
                print("Incorrect guess.")
                attempts -= 1

            guessed_letters.append(guess)
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
