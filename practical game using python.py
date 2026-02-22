import random

secret_number = random.randint(1, 100)
attempts = 0

print("Guess the secret number between 1 and 100!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    if attempts >= 8:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")
        break
