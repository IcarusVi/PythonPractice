#Game class will manage scores and Player class hands 
# Game will only consist of two players or 1 player and a bot'
# Game will keep playing until it ends

class Game:
    rounds = 0
    
    def startGame(self):
        gameType = input('Choose a game type, ')
