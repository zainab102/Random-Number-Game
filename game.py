import random

def main():
    print("Welcome to the Random Number Game!")
    print("I'm thinking of a number between 1 and 20.")
    print("You have 5 attempts to guess it. Good luck!\n")

    while True:  # Replay loop
        number = random.randint(1, 20)
        attempts = 0
        max_attempts = 5

        while attempts < max_attempts:
            try:
                guess = int(input("Guess a number between 1 and 20: "))
                if guess < 1 or guess > 20:
                    print("Please guess a number between 1 and 20.")
                    continue
                attempts += 1
                if guess == number:
                    print(f"Congratulations! You guessed it in {attempts} attempts.")
                    break
                elif guess < number:
                    print("Too low!")
                else:
                    print("Too high!")
            except ValueError:
                print("Invalid input. Please enter a number.")

        else:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
