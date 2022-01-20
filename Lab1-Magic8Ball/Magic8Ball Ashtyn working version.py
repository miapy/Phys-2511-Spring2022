from time import sleep
from random import randint

question = input("What is your question?")

print("Thinking...")
sleep(0.5)

print("Your question was", question)

x = randint(0,1)
if x == 0:
    answer = "yes"
if x == 1:
    answer = "no"

print("My answer is", answer)