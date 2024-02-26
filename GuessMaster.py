import random

def guessing_game():
    print("Welcome to the Advanced GuessMaster Challenge!")
    
    # Set difficulty level
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    max_number = 100 if difficulty == "easy" else 500 if difficulty == "medium" else 1000
    
    secret_number = random.randint(1, max_number)
    attempts = 0
    max_attempts = 20 if difficulty == "easy" else 15 if difficulty == "medium" else 10
    
    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (between 1 and {max_number}): "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number, {secret_number}!")
            print(f"Your score: {max_attempts - attempts} points")
            break
        
        attempts += 1
    
    if attempts == max_attempts:
        print(f"Game over! The correct number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    guessing_game()
