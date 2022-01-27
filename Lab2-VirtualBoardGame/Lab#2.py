#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:00:33 2022

@author: sopyt
"""

import random as rn

gameSpaces = [0]*150

for x in range(100):
    gameSpaces[x] = rn.choice([0,0,0,1])
    if gameSpaces[x] == 1:
        gameSpaces[x] = rn.choice(range(-12,12))
        if gameSpaces[x] == 0:
            gameSpaces[x] = 1
    
playerOne = input("Hello, and welcome to the game. Please enter a name for player one: \n")
playerTwo = input("Wow! What a nice name. Please enter a name for player two: \n")
print("\nWow! What a nice name. Let's commence gameplay.")

firstMove = [1,2]
firstMoveWinner = rn.choice(firstMove)
if firstMoveWinner == 1:
    print("\nBy random choice," ,playerOne, "will have the first roll.")
    x = 1
else:
    print("\nBy random choice," ,playerTwo, "will have the first roll.")
    x = 2

playerOnePosition = 1
playerTwoPosition = 1

while 1:
    
    diceNumbers = [2,3,4,5,6,7,8,9,10,11,12] #assumming 2, six-sided die
    diceRoll = rn.choice(diceNumbers)
    
    x = x + 1
    if x%2 == 0:
        print("\nTime for" ,playerOne, "to roll!")
        player = playerOne
        playerOnePosition = playerOnePosition + diceRoll
        playerPosition = playerOnePosition
    else:
        print("\nTime for" ,playerTwo, "to roll!")
        player = playerTwo
        playerTwoPosition = playerTwoPosition + diceRoll
        playerPosition = playerTwoPosition

    print(player, "has rolled" ,diceRoll)
    
    if playerPosition == 100:
        print("\nOMG!!! This means that" ,player, "has landed on space 100 and just WON the game! Congratulations!")
        break
    elif playerPosition >= 100:
        print("\nOMG!!! This means that",player,"has passed space 100 and just WON the game! Congratulations!")
        break
    
    print(player, "now moves from space" ,playerPosition - diceRoll, "to space" ,playerPosition)
    
    
    if gameSpaces[playerPosition] == 0:
        print(player, "has not landed on a special space and thus remains at space",playerPosition)
    else:
        print(player, "has just landed on a special space!")
        if gameSpaces[playerPosition] >= 1:
            print("What a lucky duck!", player, "moves forward" ,gameSpaces[playerPosition], "spaces to space" ,playerPosition + gameSpaces[playerPosition])
        else:
            print("Bad luck!",player, "moves back" ,gameSpaces[playerPosition], "spaces to space" ,playerPosition + gameSpaces[playerPosition])
            
    playerPosition = playerPosition + gameSpaces[playerPosition]
    if x%2 == 0:
        playerOnePosition = playerPosition
    else:
        playerTwoPosition = playerPosition
   
  
    
print(gameSpaces)
