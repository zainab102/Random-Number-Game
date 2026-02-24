import random

DIFFICULTIES = {
    "1": ("Easy", 20, 7),
    "2": ("Medium", 50, 6),
    "3": ("Hard", 100, 5),
}


def choose_difficulty():
    print("Choose a difficulty:")
    print("1) Easy   (1-20,  7 attempts)")
    print("2) Medium (1-50,  6 attempts)")
    print("3) Hard   (1-100, 5 attempts)")
    choice = input("Enter 1, 2, or 3 (default 1): ").strip()
    return DIFFICULTIES.get(choice, DIFFICULTIES["1"])


def get_guess(max_number):
    guess_text = input(f"Guess a number between 1 and {max_number} (or 'q' to quit round): ").strip().lower()
    if guess_text == "q":
        return None
    try:
        guess = int(guess_text)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return "invalid"
    if guess < 1 or guess > max_number:
        print(f"Please guess a number between 1 and {max_number}.")
        return "invalid"
    return guess


def play_round(max_number, max_attempts):
    number = random.randint(1, max_number)
    attempts = 0

    while attempts < max_attempts:
        guess = get_guess(max_number)
        if guess is None:
            print("Round ended early.")
            return False, attempts
        if guess == "invalid":
            continue

        attempts += 1

        if guess == number:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            return True, attempts
        if guess < number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")
    return False, attempts


def main():
    print("Welcome to the Random Number Game!")
    print("Try to guess the secret number.\n")

    games_played = 0
    wins = 0
    best_attempts = None

    while True:
        difficulty_name, max_number, max_attempts = choose_difficulty()
        print(f"\n{difficulty_name} mode selected: 1-{max_number}, {max_attempts} attempts.\n")

        won, attempts_used = play_round(max_number, max_attempts)
        games_played += 1

        if won:
            wins += 1
            if best_attempts is None or attempts_used < best_attempts:
                best_attempts = attempts_used

        print("\nStats:")
        print(f"Games played: {games_played}")
        print(f"Wins: {wins}")
        print(f"Losses: {games_played - wins}")
        if best_attempts is not None:
            print(f"Best win: {best_attempts} attempts")

        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
