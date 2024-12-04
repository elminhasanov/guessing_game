import random

def choose_level():
    """Let the user choose a difficulty level."""
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    
    while True:
        level = input("Enter 1, 2, or 3: ")
        if level == '1':
            return 10
        elif level == '2':
            return 50
        elif level == '3':
            return 100
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def play_game():
    """Main function to play the game."""
    max_number = choose_level()
    number_to_guess = random.randint(1, max_number)
    attempts = 0
    
    print(f"Guess the number between 1 and {max_number}!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}.")
                continue
            
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if play_again():
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

def play_again():
    """Ask the user if they want to play again."""
    while True:
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again in ['yes', 'y']:
            return True
        elif play_again in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()