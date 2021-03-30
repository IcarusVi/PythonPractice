# Player class is meant to play rock paper scissors 
# Player needs to be able to choose rock, paper, or scissors
# Player should have a name
class Player:
    def __init__(self, name):
        self.name = name

    #f Function to choose rock paper or scissors
    def chooseHand(self):
        hand = input('Pick your hand by typing  R(Rock), P(Paper), or S(Scissors)')
        if hand !== 'R' or hand !== 'P' or hand !== 'S':
            return False
        else:
            return hand

