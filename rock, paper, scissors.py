import random

choice = ["Rock", "Paper", "Scissors"]
choices = random.choice(choice)

playerinput = (input("Rock, Paper or Scissors? "))

if playerinput == "Rock": #If player selected rock
    if choices == "Rock": #Draw
        print("Draw")

    elif choices == "Paper": #Robot won
        print("Robot Won")

    elif choices == "Scissors": #Player won
        print("You Won")

    else: #An extremaly rare error
        print("Error")
        exit()


elif playerinput == "Paper": #If player selected paper
    if choices == "Paper": #Draw
        print("Draw")

    elif choices == "Rock": #Player won
        print("You won")

    elif choices == "Scissors": #Robot won
        print("Robot won")

    else: #Rare error
        print("Error")
        exit()



elif playerinput == "Scissors": #If player selected scissors
    if choices == "Scissors": #Draw
        print("Draw")

    elif choices == "Paper": #Player won
        print("Player won")

    elif choices == "Rock": #Robot won
        print("Robot won")

    else: #Rare error
        print("Error")
        exit()

else: #If player did not type rock paper or scissors
    print("Error, try type Rock Paper or Scissors.")
    exit()







