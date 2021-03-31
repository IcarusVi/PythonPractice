#Game class will manage scores, rounds and Player class hands 
# Game will only consist of two players or 1 player and a bot'
# Game will keep playing until it ends
from player import *


class Game:
    rounds = 0
    computerScore = 0
    playerOneScore = 0
    playerTwoScore = 0
    resume = True

    def startGame(self):
        gameType = input('Choose a game type: 1(Player vs Player) or 2(Player vs Bot)')
        ## If game type = 1 initiate PVP game, if 2 initiate Player vs Bot game
        self.pvpGame(gameType)

    def pvpGame(self, gameType):
        if gameType == '1':
            playerOneName = input('Player One pick a name: ')
            playerTwoName = input('Player Two pick a name: ')
            playerOne = Player(playerOneName)
            playerTwo = Player(playerTwoName)

            #Should probably separate this function into it's own loop
            while self.resume:
                self.rounds+=1
                self.matchUp(playerOne, playerTwo)
                continueGame = input('Enter Y to continue or Q to quit: ').upper()
                if continueGame == "Q":
                    print(f"You played {self.rounds} round(s)")
                    if self.playerOneScore == self.playerTwoScore:
                        print(self.playerOneScore)
                        print("It's a tie!")
                    elif self.playerTwoScore > self.playerOneScore:
                        print(f"{playerTwo.name} wins with a score of {self.playerTwoScore}")
                    elif self.playerTwoScore < self.playerOneScore:
                        print(f"{playerOne.name} wins with a score of {self.playerOneScore}")
                    return
            
        # This will control the bot game
        elif gameType == '2':
            playerOneName = input('Player One pick a name: ')
            playerOne = Player(playerOneName)
            playerTwo = Bot()

            while self.resume:
                self.rounds+=1
                self.matchUp(playerOne, playerTwo)
                continueGame = input('Enter Y to continue or Q to quit: ').upper()
                if continueGame == "Q":
                    print(f"You played {self.rounds} round(s)")
                    if self.playerOneScore == self.playerTwoScore:
                        print(self.playerOneScore)
                        print("It's a tie!")
                    elif self.playerTwoScore > self.playerOneScore:
                        print(f"{playerTwo.name} wins with a score of {self.playerTwoScore}")
                    elif self.playerTwoScore < self.playerOneScore:
                        print(f"{playerOne.name} wins with a score of {self.playerOneScore}")
                    return


        
            

    # Function to determine the winner from a match up
    def matchUp(self, playerOne, playerTwo):
        # In case of a tie
        playerOneHand = playerOne.chooseHand()
        playerTwoHand = playerTwo.chooseHand()
        print(playerOneHand)
        print(playerTwoHand)
        if playerOneHand == playerTwoHand:
            print(f"It's a tie play again")
        
        #When Player One picks rock
        elif playerOneHand == 'R':
            print('Rock was picked')
            if playerTwoHand =='S':
                self.playerOneScore+=1
                print(f'{playerOne.name} wins! Rock beats scissors!')
                
            else:
                self.playerTwoScore+=1
                print(f'{playerTwo.name} wins! Paper beats rock!')
                


        #When Player One picks Paper
        elif playerOneHand == 'P':
            if playerTwoHand =='R':
                self.playerOneScore+=1
                print(f'{playerOne.name} wins! Paper beats rock!')
                return
            else:
                self.playerTwoScore+=1
                print(f'{playerTwo.name} wins! Scissors beats paper!')
                return
        
        #When Play One picks Scissors
        elif playerOneHand == 'S':
            if playerTwoHand =='P':
                self.playerOneScore+=1
                print(f'{playerOne.name} wins! Scissors beats paper!')
                return
            else:
                self.playerTwoScore+=1
                print(f'{playerTwo.name} wins! Rock beats scissors!')
                return
                

        
newGame = Game()
newGame.startGame()