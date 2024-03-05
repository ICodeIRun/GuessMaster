import random
from colorama import Fore, Style, init

init(autoreset=True)

class GuessMasterChallenge:
    def __init__(self):
        self.high_score = float('inf')

    def play_game(self):
        print(Fore.MAGENTA + "*******************************************")
        print("*" + Fore.CYAN + "       Welcome to the GuessMaster        " + Fore.MAGENTA + "*")
        print("*" + Fore.CYAN + "             Advanced Challenge           " + Fore.MAGENTA + "*")
        print("*******************************************")

        # Set difficulty level
        difficulty = input(Fore.YELLOW + "Choose difficulty (easy/medium/hard): ").lower()
        max_number = 100 if difficulty == "easy" else 500 if difficulty == "medium" else 1000

        secret_number = random.randint(1, max_number)
        attempts = 0
        max_attempts = 20 if difficulty == "easy" else 18 if difficulty == "medium" else 14

        print(Fore.GREEN + "\nGet ready for a challenging game!\n")

        while attempts < max_attempts:
            guess = self.get_user_input(max_number, attempts, max_attempts)

            if guess < secret_number:
                print(Fore.RED + "Too low! Try again.")
            elif guess > secret_number:
                print(Fore.RED + "Too high! Try again.")
            else:
                print(Fore.YELLOW + "\nCongratulations! You guessed the correct number, {secret_number}!")
                score = max_attempts - attempts
                print(Fore.YELLOW + f"Your score: {score} points")

                # Update high score
                self.update_high_score(score)

                play_again = input(Fore.CYAN + "Do you want to play again? (yes/no): ").lower()
                if play_again != "yes":
                    print(Fore.GREEN + "\nThanks for playing GuessMaster! Your best score:", self.high_score, "points")
                    print(Fore.MAGENTA + "*******************************************")
                    return
                else:
                    secret_number = random.randint(1, max_number)
                    attempts = 0

            attempts += 1

        print(Fore.RED + f"\nGame over! The correct number was {secret_number}. Better luck next time!")

    def get_user_input(self, max_number, attempts, max_attempts):
        while True:
            try:
                return int(input(Fore.CYAN + f"Attempt {attempts + 1}/{max_attempts}: Enter your guess (between 1 and {max_number}): "))
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid number.")

    def update_high_score(self, score):
        if score < self.high_score:
            print(Fore.YELLOW + "\nNew high score!\n")
            self.high_score = score

if __name__ == "__main__":
    game = GuessMasterChallenge()
    game.play_game()
