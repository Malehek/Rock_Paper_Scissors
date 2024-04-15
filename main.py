# Write your solution below the starter code
# Follow the instructions in the tab to the right
# import random
import random
# Define your valid_input function below
objects = ["rock", "paper", "scissors"]
computer = random.choice(objects)
running = True

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

# Get a choice from the user
while running:
  user = input("rock, paper, or scissors? ").lower()
  print(f"You chose {user}")
  print(f"The computer chooses {computer}")
  
  # Compare the user and computer choice
  if user == computer:
    print("It's a draw!")
  elif user == "rock" and computer == "scissors":
    print("rock smashes scissors. You win!")
  elif user == "rock" and computer == "paper":
    print("paper covers rock. You lose!")
  elif user == "paper" and computer == "rock":
    print("paper covers rock. You win!")
  elif user == "paper" and computer == "scissors":
    print("scissors cuts paper. You lose!")
  elif user == "scissors" and computer == "paper":
    print("scissors cuts paper. You win!")
  elif user == "scissors" and computer == "rock":
    print("rock smashes scissors. You lose!")
  else:
    print("Invalid input. Please try again.")

  # Ask the user if they want to play again
  play_again = input("Do you want to play again? (y/n) ").lower()
  if not play_again == "y":
    running = False

print("Thanks for playing. Goodbye!")
# Print the right message, based on the choices
