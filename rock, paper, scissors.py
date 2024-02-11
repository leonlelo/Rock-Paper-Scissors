import random

choice = ["Rock", "Paper", "Scissors"]
choices = random.choice(choice)

playerinput = (input("Rock, Paper or Scissors? "))

if playerinput == "Rock": #If player selected rock
    if choices == "Rock": #Draw
        print("Robot:",choices)
        print("Player:",playerinput)
        print("It's a draw")

    elif choices == "Paper": #Robot won
        print("Robot:", choices)
        print("Player:", playerinput)
        print("It's a victory for the player!")

    elif choices == "Scissors": #Player won
        print("Robot:",choices)
        print("Player:",playerinput)
        print("It's victory for the robot!")

    else: #An extremely rare error
        print("Error")
        exit()


elif playerinput == "Paper": #If player selected paper
    if choices == "Paper": #Draw
        print("Robot:", choices)
        print("Player:", playerinput)
        print("Draw")

    elif choices == "Rock": #Player won
        print("Robot:", choices) 
        print("Player:", playerinput) 
        print("You won") 

    elif choices == "Scissors": #Robot won
        print("Robot:", choices)
        print("Player:", playerinput)
        print("Robot won")

    else: #Rare error
        print("Error")
        exit()

elif playerinput == "Scissors": #If player selected scissors
    if choices == "Scissors": #Draw
        print("Robot:", choices)
        print("Player:", playerinput)
        print("Draw")

    elif choices == "Paper": #Player won
        print("Robot:", choices)
        print("Player:", playerinput)
        print("Player won")

    elif choices == "Rock":
        print("Robot:", choices)
        print("Player:", playerinput)
        print("Robot won")

    else: #Rare error
        print("Error")
        exit()

else: #If player did not type rock paper or scissors
    print("Error, try type Rock Paper or Scissors, remember captital letters first.")
    exit()
