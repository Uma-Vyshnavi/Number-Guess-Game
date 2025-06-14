import random

def number_guess_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("Choose a difficulty level:\n1. Easy (1–10)\n2. Medium (1–50)\n3. Hard (1–100)")
    
    difficulty = input("Enter level (1/2/3): ")
    
    if difficulty == '1':
        max_number = 10
        attempts_allowed = 5
    elif difficulty == '2':
        max_number = 50
        attempts_allowed = 7
    elif difficulty == '3':
        max_number = 100
        attempts_allowed = 10
    else:
        print("Invalid choice. Defaulting to Easy.")
        max_number = 10
        attempts_allowed = 5

    secret_number = random.randint(1, max_number)
    attempts = 0
    score = 100

    print(f"\n🔢 I have selected a number between 1 and {max_number}. Try to guess it!")

    while attempts < attempts_allowed:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{attempts_allowed}: Your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"🎉 Correct! You guessed it in {attempts} tries. Final Score: {score}")
                break
            elif guess < secret_number:
                print("📉 Too low!")
                score -= 10
            else:
                print("📈 Too high!")
                score -= 10

        except ValueError:
            print("❌ Please enter a valid number.")

    else:
        print(f"\n❗ You've used all your attempts. The correct number was {secret_number}. Final Score: {score}")

if __name__ == "__main__":
    number_guess_game()
