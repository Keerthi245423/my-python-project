import random

def get_computer_choice():
    """Randomly selects Rock, Paper, or Scissors for the computer."""
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    """Determines the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Runs the Rock-Paper-Scissors game."""
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
    
    if user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
play_game()
