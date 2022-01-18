# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random as rn
import time as tm

userQuestion = input("What is your question? Please enter here: ")

print("I am thinking")
tm.sleep(1)
print(".")
tm.sleep(1)
print(".")
tm.sleep(1)
print(".")
tm.sleep(0.5)

print("You are asking the question: \"" + userQuestion + "\"")
print("My answer for you is: ")

tm.sleep(2)
magicalAnswer = ["Yes.", "No.", "Maybe.", "Ask again later :p", "Help! I'm trapped in a computer!!"]

print("\"" + rn.choice(magicalAnswer) + "\"")
