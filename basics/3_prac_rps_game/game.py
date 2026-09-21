from random import choice,random,shuffle

options = ["rock", "paper", "scissors"]

def play():
    print("Welcome to the game!")

    user_input = input("Enter rock, paper, or scissors: ")
    if user_input not in options:
        print("Invalid input. Please try again.")
        return
    
    computer_choice = choice(options)
    # computer_choice = options[int(random() * 3)]  
    # This line is commented out, but it can be used as an alternative way to select the computer's choice. 

    print(f"Computer chose: {computer_choice}")
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!") 

