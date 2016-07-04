import sys

#from tkinter import *
#from tkinter.ttk import *

from tkinter import *
from copy import deepcopy

#should probs move this into a game class
#information 
nplayer = -1
player1 = 0
player2 = 1
player1_icon = "X"
player2_icon = "O"
nplayer_icon = " "
player1_color = "red"
player2_color = "blue"
nplayer_color = "green"
winning_color = "gold"

#information relevant to each game
class Game:
    root = None
    mainFrame = None
    starting_player = player1
    curr_player = starting_player

    board_width = 30
    board_height = 15

    player1_moves = None
    player2_moves = None
    
    board = None

    x_position = -1
    y_position = -1
    
    game = None

    p1comboMoves = None
    p2comboMoves = None
    
    def __init__(self):
        self.showStartMenu()

    def run(self):
        self.root.mainloop()
	
    def reset(self):
        self.board = [[nplayer for x in range(self.board_height)] for x in range(self.board_width)]
        self.curr_player = player1

        if self.mainFrame != None:
            self.mainFrame.destroy()
        else:
            self.root = Tk() 
        
        self.mainFrame = GameWindow(self.root, self)

        self.player1_moves = []
        self.player2_moves = []
        self.p1comboMoves = []
        self.p2comboMoves = []
        
    def showStartMenu(self):
        if self.mainFrame != None:
            self.mainFrame.destroy()
        else:
            self.root = Tk() 
        
        self.mainFrame = GameMenuWindow(self.root, self)
        
    def startGame(self):
        self.reset()
        
    def checkWinner(self, board):
		
        x_position = self.x_position
        y_position = self.y_position
        
        #horizontally
        combo_p1 = 0;
        combo_p2 = 0;
        
        p1comboMoves = []
        p2comboMoves = []
        
        for i in range(max(x_position-5,0), min(x_position+5, self.board_width-1)):
            if board[i][y_position] == player1:
                combo_p1 = combo_p1 + 1
                combo_p2 = 0
                
                p1comboMoves.append((i, y_position))
                p2comboMoves = []
            elif board[i][y_position] == player2:
                combo_p2 = combo_p2 + 1
                combo_p1 = 0
                
                p2comboMoves.append((i, y_position))
                p1comboMoves = []
            else:
                combo_p1 = 0
                combo_p2 = 0
                
                p1comboMoves = []
                p2comboMoves = []

            if combo_p1 == 5:
                self.p1comboMoves = p1comboMoves
                return player1
            elif combo_p2 == 5:
                self.p2comboMoves = p2comboMoves
                return player2
           
        
        #vertically            
        combo_p1 = 0
        combo_p2 = 0
        
        p1comboMoves = []
        p2comboMoves = []
        
        for j in range(max(y_position-5,0), min(y_position+5, self.board_height-1)):
            if board[x_position][j] == player1:
                combo_p1 = combo_p1 + 1
                combo_p2 = 0
                
                p1comboMoves.append((x_position, j))
                p2comboMoves = []
            elif board[x_position][j] == player2:
                combo_p2 = combo_p2 + 1
                combo_p1 = 0
                
                p2comboMoves.append((x_position, j))
                p1comboMoves = []
            else:
                combo_p1 = 0
                combo_p2 = 0
                
                p1comboMoves = []
                p2comboMoves = []
                
            if combo_p1 == 5:
                self.p1comboMoves = p1comboMoves
                return player1
            elif combo_p2 == 5:
                self.p2comboMoves = p2comboMoves
                return player2
                

        #diagonally south east        
        combo_p1 = 0
        combo_p2 = 0
        
        p1comboMoves = []
        p2comboMoves = []
        
        x = max(x_position-5,0)
        y = max(y_position-5,0)
                
        x_short_fall = abs(x - (x_position-5))
        y_short_fall = abs(y - (y_position-5))

        subtractFrom = 5 - max(x_short_fall, y_short_fall)
        
        x = x_position - subtractFrom
        y = y_position - subtractFrom
        
        while x < min(x_position+5, self.board_width) and y < min(y_position+5,self.board_height):

            if board[x][y] == player1:
                combo_p1 = combo_p1 + 1
                combo_p2 = 0
                
                p1comboMoves.append((x, y))
                p2comboMoves = []
            elif board[x][y] == player2:
                combo_p2 = combo_p2 + 1
                combo_p1 = 0
                
                p2comboMoves.append((x, y))
                p1comboMoves = []
            else:
                combo_p1 = 0
                combo_p2 = 0

                p1comboMoves = []
                p2comboMoves = []
            if combo_p1 == 5:
                self.p1comboMoves = p1comboMoves
                return player1
            elif combo_p2 == 5: 
                self.p2comboMoves = p2comboMoves
                return player2

            x = x + 1
            y = y + 1
                
        
        #diagonally south west horizontally starting
        combo_p1 = 0
        combo_p2 = 0
        
        p1comboMoves = []
        p2comboMoves = []
        
        x = min(x_position+5, self.board_width-1)
        y = max(y_position-5, 0)
        
        x_short_fall = abs(x - (x_position+5))
        y_short_fall = abs(y - (y_position-5))
        
        subtractFrom = 5 - max(x_short_fall, y_short_fall)
        
        x = x_position + subtractFrom
        y = y_position - subtractFrom
            
        combo_p1 = 0
        combo_p2 = 0
            
        while x >= max(x_position-5,0) and y < min(y_position+5, self.board_height):
                
            if board[x][y] == player1:
                combo_p1 = combo_p1 + 1
                combo_p2 = 0
                
                p1comboMoves.append((x, y))
                p2comboMoves = []
            elif board[x][y] == player2:
                combo_p2 = combo_p2 + 1
                combo_p1 = 0
                
                p2comboMoves.append((x, y))
                p1comboMoves = []
            else:
                combo_p1 = 0
                combo_p2 = 0

                p1comboMoves = []
                p2comboMoves = []
                
            if combo_p1 == 5:
                self.p1comboMoves = p1comboMoves
                return player1
            elif combo_p2 == 5:
                self.p2comboMoves = p2comboMoves
                return player2    

            x = x - 1
            y = y + 1
                    
    def updateGameWinState(self):
        winner = self.checkWinner(self.board)

        if winner == player1:
            winMessage = "Winner is " + player1_icon
            self.mainFrame.changeGameMessage(winMessage)
            self.mainFrame.disableAllButtons()
            
            #highlight winning combo
            for i in range(5):
                move = self.p1comboMoves[i]
                print("win p1 combo:", move[0], move[1])
                
                comboButton = self.mainFrame.gameWidgets[move[0]][move[1]]
                comboButton.updateColor(winning_color)
                
        elif winner == player2:     
            winMessage = "Winner is " + player2_icon
            self.mainFrame.changeGameMessage(winMessage)
            self.mainFrame.disableAllButtons()

            #highlight winning combo
            for i in range(5):
                move = self.p2comboMoves[i]
                print("win p2 combo:", move[0], move[1])
                                
                comboButton = self.mainFrame.gameWidgets[move[0]][move[1]]
                comboButton.updateColor(winning_color)
        else:
            defaultMessage = "Have Fun! Copyright Felix Phu"
            self.mainFrame.changeGameMessage(defaultMessage)
            self.mainFrame.enableAllButtons()

            #remove winning combo and set it to null
            if len(self.p2comboMoves) == 5:
                for i in range(5):
                    move = self.p2comboMoves[i]
                    print("removing p2 combo:",move[0], move[1])
                                    
                    comboButton = self.mainFrame.gameWidgets[move[0]][move[1]]
                    if self.board[move[0]][move[1]] == player2:
                        comboButton.updateColor(player2_color)
                self.p2comboMoves = []

            elif len(self.p1comboMoves) == 5:
                for i in range(5):
                    move = self.p1comboMoves[i]
                    print("removing p1 combo:", move[0], move[1])
                                    
                    comboButton = self.mainFrame.gameWidgets[move[0]][move[1]]

                    if self.board[move[0]][move[1]] == player1:
                        comboButton.updateColor(player1_color)
                self.p1comboMoves = []

    
    def updateGame(self):

        self.updateGameWinState()    

        newGameAI = gameAI(self)

        newGameAI.makeMove()
        
        if self.curr_player == player1:
            self.curr_player = player2
        elif self.curr_player == player2:
            self.curr_player = player1

    def makeMove(self, x, y):
        #add move to board
        self.x_position = x
        self.y_position = y

        curr_player = self.curr_player
        self.board[self.x_position][self.y_position] = curr_player

        #update color
        if curr_player == player1:
            self.mainFrame.gameWidgets[self.x_position][self.y_position].updateText(player1_icon)
            self.mainFrame.gameWidgets[self.x_position][self.y_position].updateColor(player1_color)
            
            self.player1_moves.append((self.x_position, self.y_position))
        elif curr_player == player2:
            self.mainFrame.gameWidgets[self.x_position][self.y_position].updateText(player2_icon)
            self.mainFrame.gameWidgets[self.x_position][self.y_position].updateColor(player2_color)
            
            self.player2_moves.append((self.x_position, self.y_position))
        else: 
            self.mainFrame.gameWidgets[self.x_position][self.y_position].updateText(nplayer_icon)
            self.mainFrame.gameWidgets[self.x_position][self.y_position].updateColor(nplayer_color)

        #disable the button
        self.mainFrame.gameWidgets[self.x_position][self.y_position].disableButton()
        
        self.updateGame()

    def undoLastMove(self):

        #retrieve last move
        last_move = None

        if self.curr_player == player1:
            if len(self.player2_moves) == 0:
                return
            last_move = self.player2_moves.pop()
            self.curr_player = player2
        elif self.curr_player == player2:
            if len(self.player1_moves) == 0:
                return
            last_move = self.player1_moves.pop()
            self.curr_player = player1

        last_x_move = last_move[0]
        last_y_move = last_move[1]

        self.board[last_x_move][last_y_move] = nplayer
   
        #Modify widget to be set to nplayer
        self.mainFrame.gameWidgets[last_x_move][last_y_move].updateText(nplayer_icon)
        self.mainFrame.gameWidgets[last_x_move][last_y_move].updateColor(nplayer_color)    
        self.mainFrame.gameWidgets[last_x_move][last_y_move].enableButton()

        self.updateGameWinState()

class squareFrameWithButton(Frame):

    button1 = None
    
    def __init__(self, parent, col, row, *args, **kwargs):
        Frame.__init__(self, parent, width=40, height=40)
        #Button.__init__(self, parent,**kwargs)
        self.button1 = gameButton(self, col, row, **kwargs)
        
        self.grid_propagate(False)          #disables resizing of frame
        self.columnconfigure(0, weight=1)   #enables button to fill frame
        self.rowconfigure(0,weight=1)       #any positive number would do the trick

        self.grid(row=0, column=1)          #put frame where the button should be
        self.button1.grid(sticky="wens") 

        self.button1.bind("<Button-1>", parent.buttonClick) #the underlying button becomes the event widget instead
        
        #self.pack()
       
    def updateText(self, new_text):
        self.button1.updateText(new_text)

    def updateColor(self, color):
        self.button1.updateColor(color)

    def disableButton(self):
        self.button1.disableButton()
        
    def enableButton(self):
        self.button1.enableButton()

    def getText(self):
        return self.button1.cget("text")
    
class gameButton(Frame):

    parent_frame = None
    row = -1
    col = -1
    name = "gameButton"
    disabled = False
    
    def __init__(self, parent, col, row, *args, **kwargs):
        Frame.__init__(self, parent, width=40, height=40)
        Button.__init__(self, parent, **kwargs)

        self.parent_frame = parent
        
        self.row = row
        self.col = col
       
    def updateText(self, new_text):
        self.configure(text=new_text)

    def updateColor(self, color):
        self.configure(bg=color)
        
    def disableButton(self):
        self.disabled = True
    
    def enableButton(self):
        self.disabled = False

class GameMenuWindow(Frame):
    buttonSize = 0
    game = None
    
    def __init__(self, parent, game):
        Frame.__init__(self, parent, width=700,height=300)

        self.game = game
        
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):

        self.parent.title("Five in a Row")
		
        startGameBttn = Button(self, text="Start", command=self.game.startGame)
        optionsBttn = Button(self, text="Options", command=self.quit)
        self.gameMessages = Label(self, text="Have Fun! Copyright Felix Phu")

        self.ButtonSize = int(self.game.board_width/3)
        buttonStartX = int(self.game.board_width/2) - int(self.ButtonSize/2)
        buttonStartY = int(self.game.board_height/2) - int(self.ButtonSize/2)
        
        startGameBttn.grid(row=buttonStartY, column=buttonStartX, columnspan=self.ButtonSize, sticky=W+E)
        optionsBttn.grid(row=buttonStartY+3, column=buttonStartX, columnspan=self.ButtonSize, sticky=W+E)
        
        #self.gameMessages.grid(row=board_height+1, columnspan=board_width, sticky=W+E)
        

                
        self.pack()
    
    def centerWindow(self):
      
        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

#the main tkinter frame that modifies the game
class GameWindow(Frame):
    
    #reference to parent game
    game = None
    
    #Game message label
    gameMessages = None

    #Grid Button Widget dictionary
    gameWidgets = None

    #disabled buttons?
    disabledGame = False
    
    def __init__(self, parent, game):
        Frame.__init__(self, parent)

        self.game = game

        self.gameWidgets = [[None for x in range(self.game.board_height)] for x in range(self.game.board_width)]
	
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):
        board = self.game.board
		
        #self.pack(fill=tk.BOTH, expand=1)

        self.parent.title("Five in a Row")
		
        # organise buttons in the frame container
        #configure the Button widget to have a specific font and padding
        #Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        #we use colconffig and rowconfig to define space in grid columns and rows
        #e.g.  here buttons are seperated by some space
       
        #entry widgets are where digits are displayed
        #they may not occupy all the space allocated
        #we set sticky to expand from left to right
        #entry = Entry(self)

        restartbttn = Button(self, text="Restart", command=self.game.reset)
        undobuttn = Button(self, text="Undo", command=self.game.undoLastMove)
        self.gameMessages = Label(self, text="Have Fun! Copyright Felix Phu")

        half_board = int(self.game.board_width/2)     
        restartbttn.grid(row=0, columnspan=half_board, sticky=W+E)
        undobuttn.grid(row=0,column=half_board, columnspan=half_board, sticky=W+E)
        self.gameMessages.grid(row=self.game.board_height+1, columnspan=self.game.board_width, sticky=W+E)
        
        #create buttons and set them in the appropriate grids
        
        for i in range(self.game.board_height):
            for j in range(self.game.board_width):
                but = None
                if board[j][i] == player1:
                    but = squareFrameWithButton(self, j, i, text=player1_icon, bg=player1_color)    
                elif board[j][i] == player2:
                    but = squareFrameWithButton(self, j, i, text=player2_icon, bg=player2_color)
                else:
                    but = squareFrameWithButton(self, j, i, text=nplayer_icon, bg=nplayer_color)
                    
                but.grid(row=i+1, column=j)
                self.gameWidgets[j][i] = but
                
        self.pack()
      
		
    def centerWindow(self):
      
        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def buttonClick(self, event):
        board = self.game.board
        x_move = event.widget.col
        y_move = event.widget.row
	
        if event.widget.disabled:
            return

        self.game.makeMove(x_move, y_move)

    def changeGameMessage(self, newMessage):
        self.gameMessages.configure(text=newMessage)

    def disableAllButtons(self):
        if self.disabledGame == True:
            return
        
        self.disabledGame = True
        for i in range(self.game.board_height):
            for j in range(self.game.board_width):

                self.gameWidgets[j][i].disableButton()
                
    def enableAllButtons(self):
        if self.disabledGame == False:
            return
        
        self.disabledGame = False
        for i in range(self.game.board_height):
            for j in range(self.game.board_width):
                if self.gameWidgets[j][i].getText() == nplayer_icon:
                    self.gameWidgets[j][i].enableButton()
                
                

####game AI
#Ai that when given a game board and the player number produces a move that is best


#def minMaxGameMove(gameBoard, human_player_icon, computer_player_icon):


#zdef minMove(gameBoard):


class gameAI:
    gameBoard = None
    game = None
    playerUserIcon = None
    playerAIIcon = None

    def __init__(self, game):
        self.game = game

        #have these be given by the given game class
        playerUserIcon = "X"
        playerAIIcon = "O"

    def makeMove(self):
        gameBoard = deepcopy(self.game.board)
        gameBoard[1][1] = self.playerAIIcon
        #return self.minMove((0,0), 0)

    #note this is the user player
    def minMove(self, move, currDepth): 
        #add move to the game board
        self.gameBoard[move[0]][move[1]] = playerUserIcon
        
        #check if winning move or depth reached

        #if so, return the calculated heuristic


        #generate child moves and choose the move with the smallest returned value
        currMinMove = None
        currMinMoveVal = 9999999 #number that must be replaced
        
        for j in range(self.game.board_height):
            for i in range(self.game.board_width):

                #if the board grid square is empty it is a possible move
                if self.gameBoard[i][j] == nplayer:

                    val = self.maxMove((i, j), currDepth + 1)

                    if val < smallestVal:
                        currMinMove = (i, j)
                        
                    
        #remove move from the game board

        #now we return the move value
        return currMinMoveVal
    
        

##game loop
    ##grab input
    ##update game
    ##display game

stillPlaying = True

def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
