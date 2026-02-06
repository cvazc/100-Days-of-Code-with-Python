import random
import art

def check_win_or_lose(attempts, computer_guess_number):
    while attempts > 0:
        user_guess = int(input("Make a guess: "))

        if user_guess == computer_guess_number:
            print(f"You win! The number was {computer_guess_number}")
            return
        elif user_guess > computer_guess_number:
            print("Too High")
        else:
            print("Too Low")

        attempts -= 1
        if attempts > 0:
            print("Guess again.")
    
    print(f"You lose. The number was {computer_guess_number}.")

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    
    number_to_guess = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == "hard":
        attempts = 5
    else:
        attempts = 10
    
    check_win_or_lose(attempts, number_to_guess)

play_game()