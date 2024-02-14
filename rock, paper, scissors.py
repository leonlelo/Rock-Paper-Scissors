import random

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'


choice = ["Rock", "Paper", "Scissors"]
choices = random.choice(choice)

playerinput = (input("Rock, Paper or Scissors? "))

if playerinput == "Rock": #If player selected rock
    if choices == "Rock": #Draw
        print(RED + "Robot:",choices + RESET)
        print(GREEN + "Player:",playerinput + RESET)
        print(BLUE + "It's a draw" + RESET)

    elif choices == "Paper": #Robot won
        print(CYAN + "Robot:", choices + RESET)
        print(GREEN + "Player:", playerinput + RESET)
        print(BLUE + "It's a victory for the player!" + RESET)

    elif choices == "Scissors": #Player won
        print(YELLOW + "Robot:",choices + RESET)
        print( CYAN +"Player:",playerinput + RESET)
        print(RED + "It's victory for the robot!" + RESET)

    else: #An extremely rare error
        print("Error")
        exit()


elif playerinput == "Paper": #If player selected paper
    if choices == "Paper": #Draw
        print("Robot:", choices)
        print("Player:", playerinput)
        print("Its a draw!")

    elif choices == "Rock": #Player won
        print("Robot:", choices) 
        print("Player:", playerinput) 
        print("Its an victory for the player!") 

    elif choices == "Scissors": #Robot won
        print("Robot:", choices)
        print("Player:", playerinput)
        print("Its a victory for the robot!")

    else: #Rare error
        print("Error!")
        exit()



elif playerinput == "Scissors": #If player selected scissors
    if choices == "Scissors": #Draw
        print("Robot:", choices)
        print("Player:", playerinput)
        print("Its an intens draw!")

    elif choices == "Paper": #Player won
        print("Robot:", choices)
        print("Player:", playerinput)
        print("The player won!")

    elif choices == "Rock": #Robot won
        print("Robot:", choices)
        print("Player:", playerinput)
        print("Its an intens victory for the robot!")

    else: #Rare error
        print("Error!")
        exit()

else: #If player did not type rock paper or scissors
    print("Error, try type Rock Paper or Scissors, remember captital letters first!")
    exit()

