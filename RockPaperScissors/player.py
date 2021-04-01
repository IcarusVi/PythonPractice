# Player class is meant to play rock paper scissors 
# Player needs to be able to choose rock, paper, or scissors
# Player should have a name
import random

class Player:
    def __init__(self, name):
        self.name = name

    #f Function to choose rock paper or scissors
    def chooseHand(self):
        hand = input(self.name + ' pick your hand by typing  R(Rock), P(Paper), or S(Scissors)').upper()
        #Checks if the input only uses R, P, or S
        if hand in 'R,P,S':
            return hand
        else:
            return False


# Bot class randomly picks Rock Paper or Scissors represented by R, P, and S
class Bot(Player):
    def __init__(self):
        self.name = 'Bot'
    
    totalMoves = ['R', 'P', 'S']

    # Function to pick a random letter from the total moves list;
    # could've used random.choice as well
    def chooseHand(self):
        hand = self.totalMoves[random.randint(0,2)]
        return hand