from random import randint
import numpy as np
import time as tt

#Number of Players input
NumOfPlayers = input("Welcome. How many players are there? ")
NumOfPlayers = int(NumOfPlayers)

#Saves Space location
Space = np.arange(NumOfPlayers)

#Sets max players for loop and properlly states NumOfPlayers
MaxPlayers = NumOfPlayers - 1
NumOfPlayers = NumOfPlayers + 1
Players = np.arange (1,NumOfPlayers,1)

#Sets board spaces
Board = np.arange (1,101,1)

#Sets up Win status and player for start
Win = 0
CurrentPlayer = 0

#Turn based system loop
while Win == 0:
    print("It is player ", Players[CurrentPlayer], "'s turn. Rolling dice...") #Rolling dice and updating position
    tt.sleep(0.5) #Slows down die roll
    Dice = randint(1,6) #randomizes roll number
    print("You rolled a ", Dice, ".")
    Space[CurrentPlayer] = Space[CurrentPlayer] + Dice #Adds roll to space for player
    if Space[CurrentPlayer] >= 100: #Checks if player reached 100
        print("Player ", Players[CurrentPlayer], " wins!") #Tells player they won
        Win = 1 #stops loop if player wins
    elif Space[CurrentPlayer] % 3 == 0 and Space[CurrentPlayer] > 6: #Checks for special space
        x = randint(0,1) #randomizes Chute or Ladder
        if x == 1: #Sets ladder rules
            y = randint(1,6)
            Space[CurrentPlayer] = Space[CurrentPlayer] + y
            print("Player ", Players[CurrentPlayer], "landed on a ladder. Move forward ", y, "spaces! You are now on space ", Space[CurrentPlayer], ".")
            if Space[CurrentPlayer] >= 100: #restates win rules
                print("Player ", Players[CurrentPlayer], " wins!")
                Win = 1
        else:
            y = randint(1,6) #Sets Chute rules
            Space[CurrentPlayer] = Space[CurrentPlayer] - y
            print("Player ", Players[CurrentPlayer], "landed on a chute. Move back ", y, "spaces. You are now on space ", Space[CurrentPlayer], ".")
            if Space[CurrentPlayer] >= 100: #restates win rules
                print("Player ", Players[CurrentPlayer], " wins!")
                Win = 1
    if Win == 0:
        print("Player ", Players[CurrentPlayer], "is on space ", Space[CurrentPlayer], ".") #states player space
    CurrentPlayer = CurrentPlayer + 1 #Mkaes current player the next player
    #Make sure we do not run out of players
    if CurrentPlayer > MaxPlayers: #returns to 1st player after last player
            CurrentPlayer = 0

