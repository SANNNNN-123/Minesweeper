from game import Game
from board import Board

#-----Easy
#size = (9,9) , screenSize = (400,400)
#-----Medium
#size = (20,50) , screenSize = (1700,800)

size = (20,50) 
prob = 0.1

board = Board(size,prob)
screenSize = (1200,600)
game = Game(board,screenSize)
game.run()