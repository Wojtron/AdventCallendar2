# This is a sample Python script.
import random


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():




def comparisons(userFigure, computerFigure):

    userScore = 0
    computerScore = 0


    winScore = 6
    drawScore = 3
    looseScore = 0
    rockScore = 1
    paperScore = 2
    scissorsScore = 3


    if userFigure == "paper" and computerFigure == "scissors":
        userScore =   looseScore + paperScore
        computerScore =   winScore + scissorsScore
    elif  userFigure == "paper" and computerFigure == "rock":
        userScore =  + winScore + paperScore
        computerScore =   looseScore + rockScore
    elif userFigure== "paper" and computerFigure == "paper":
        userScore =   drawScore + paperScore
        computerScore =  drawScore + paperScore

    elif  userFigure == "rock" and computerFigure == "paper":
        userScore =  looseScore + rockScore
        computerScore =  winScore + paperScore
    elif userFigure== "rock" and computerFigure == "scissors":
        userScore =   winScore + rockScore
        computerScore = looseScore + scissorsScore
    elif userFigure == "rock" and computerFigure == "rock":
        userScore = drawScore + rockScore
        computerScore = drawScore + rockScore

    elif userFigure == "scissors" and computerFigure == "paper":
        userScore =  winScore + scissorsScore
        computerScore = looseScore + paperScore
    elif userFigure == "scissors" and computerFigure == "rock":
        userScore =  looseScore + scissorsScore
        computerScore = winScore + rockScore
    elif userFigure == "scissors" and computerFigure == "scissors":
        userScore = drawScore + scissorsScore
        computerScore =  drawScore + scissorsScore

        return




def strategy():

    figures = ["rock","paper","scisors"]

    computerChoice = ""
    userChoice = ""
    A = figures[0]
    Z = figures[0]
    B = figures[1]
    X = figures[1]
    C = figures[2]
    Y = figures[2]

    computerChoice = random.choice(figures)
    userFigure = ""

    print(computerChoice)

    if computerChoice == "paper":
        userFigure = X
        comparisons(userFigure,computerChoice)
    elif computerChoice == "scissors":
        userFigure = Y
    else:
        userFigure = Z




def print_hi(name):

    print("xcxcxcx")
