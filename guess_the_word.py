import random

# List of words to choose from
word_list = ["python", "programming", "computer", "gaming", "coding", "keyboard", "challenge"]

# Function to choose a random word
def choose_word():
    return random.choice(word_list)

# Function to play the game
def play_game():
    secret_word = choose_word()
    guessed_word = "_" * len(secret_word)
    attempts = 6  # You can customize the number of attempts

    print("Welcome to Guess the Word!")
    print("Try to guess the secret word one letter at a time.")
    print("You have", attempts, "attempts to guess the word.")

    while attempts > 0:
        print("\nCurrent word:", guessed_word)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word = guessed_word[:i] + guess + guessed_word[i + 1:]
            if guessed_word == secret_word:
                print("Congratulations! You guessed the word:", secret_word)
                break
        else:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts remaining.")

    if attempts == 0:
        print("Out of attempts! The secret word was:", secret_word)

if __name__ == "__main__":
    play_game()
￼Enter
