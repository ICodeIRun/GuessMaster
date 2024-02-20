import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    secret_number = random.randint(1, 100)
    
    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number, {secret_number}!")
            break

if __name__ == "__main__":
    guessing_game()
