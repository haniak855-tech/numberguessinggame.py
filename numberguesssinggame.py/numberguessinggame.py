import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100.")
    print("Can you guess it?\n")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} — Your guess: "))
        except ValueError:
            print("⚠️  Please enter a valid number!\n")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try higher.\n")
        elif guess > secret_number:
            print("📈 Too high! Try lower.\n")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts!")
            break
    else:
        print(f"😢 Out of attempts! The number was {secret_number}.")

    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing! 👋")

number_guessing_game()