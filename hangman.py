import random

def get_word():
    words = ["python", "hangman", "challenge", "programming", "computer"]
    return random.choice(words)

def display(word, guessed):
    return " ".join([c if c in guessed else "_" for c in word])

def hangman():
    word = get_word()
    guessed = set()
    attempts = 6

    print("Welcome to Hangman!")
    while attempts > 0:
        print(f"\nWord: {display(word, guessed)}")
        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            print("Already guessed.")
        elif guess in word:
            guessed.add(guess)
            if all(c in guessed for c in word):
                print(f"\nWord: {word}")
                print("Congratulations! You won!")
                break
        else:
            guessed.add(guess)
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()