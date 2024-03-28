import pygame
import os

class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        #pieceSize is size of board divide by row,column
        #height divide by row, width divide by column
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1] , self.screenSize[1] // self.board.getSize()[0]
        self.LoadImages()

    def run(self):
        icon = pygame.image.load("icon.png")
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Minesweeper")
        
        pygame.init()   

        self.screen = pygame.display.set_mode(self.screenSize) 
        running = True
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running=False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position,rightClick)

            self.draw()
            pygame.display.flip()
            if (self.board.getWon()):
                #insert sound if win

                running = False 
        pygame.quit()

    def draw(self):
        topLeft = (0,0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row,col))
                image = self.getImage(piece)    
                #image = self.images["empty-block"]
                self.screen.blit(image,topLeft)
                topLeft = topLeft[0] + self.pieceSize[0] , topLeft[1] #col is increment by pieceSize width
            topLeft = 0, topLeft[1] + self.pieceSize[1] #row is increment by pieceSize height

    def LoadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece):
        #string = "unclicked-bomb" if piece.getHasBomb() else "empty-block"
        #string = "unclicked-bomb" if piece.getHasBomb() else str(piece.getNumAround())
        string = None
        if (piece.getClicked()):
            string = "bomb-at-clicked-block" if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = "flag" if piece.getFlagged() else "empty-block"

        return self.images[string]

    def handleClick(self,position,rightClick):
        if (self.board.getLost()):
            return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)
        
        
        #print(index)