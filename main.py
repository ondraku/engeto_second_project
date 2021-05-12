import random

ODDELOVAC = "=" * 100

def welcome():
    print("Hi there! Welcome to the Bulls & Cows game!")
    print(ODDELOVAC)
    print("I've generated a random 4 digit number for you. Can you guess it?\n"
          "Let's play the game!")
    print(ODDELOVAC)
    return()

welcome()