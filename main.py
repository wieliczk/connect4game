import sys
""" Main game for Connect Four game
	Game Requires no input as it is 8 long and 8 high"""

MAXHEIGHT = 8
MAXROW = 8
ACCEPTED = [0,1,2,3,4,5,6,7]
QUITS = "exit"
SUCCESS = 1
FAIL = 0
PLAYERONE = "x"
PLAYERTWO = "o"

class Board:
	""" Board for the game"""
	
	# Only contains a list of lists. 
	def __init__(self):
		self.bRows = []
	
	# Sets up Lists
	def createBoard(self):
		for i in range(MAXROW):
			self.bRows.append([])
	
	# Adds players move list
	def chosenMove(self, choice, player):
		if not len(self.bRows[choice]) >= MAXHEIGHT:
			if player == 0:
				self.bRows[choice].append(PLAYERONE)
			else:
				self.bRows[choice].append(PLAYERTWO)
			return SUCCESS
		else:
			return FAIL
	
	# For testing
	def tprintb(self):
		print(self.bRows)
	# Draws Board 
	def drawBoard(self):
		beforebottom = "-------------------"
		bottomline = "| 0 1 2 3 4 5 6 7 |"
		largestBin = [0,0] # [len(bin), bin number]
		for i in range(MAXROW):
			if largestBin[0] <= len(self.bRows[i]):
				largestBin = [len(self.bRows[i]), i]
		for i in range(largestBin[0]-1, -1, -1):
			line = "| "
			for x in range(MAXROW):
				try:
					piece = self.bRows[x][i]
					piece += " "
					line += piece
				except:
			  		line += "  "
			line += "|"
			print(line)	
		print(beforebottom)
		print(bottomline)		
		
# Where the player chooses which row to drop a piece in
def makeMove(player):
	while True:
		if player == 1:
			turn = "Player 2: "
		if player == 0:
			turn = "Player 1: "
		try:
			Pchoice = input(turn + "Pick a number on the board from 0-7 to make a move and 'exit' to quit: ")
			if Pchoice == QUITS: # Exits
				break
			if int(Pchoice) in ACCEPTED:
				break
			else:
				raise Exception
		except:
			print("Incorrect input")	
	return Pchoice

# Checks if player 
def checkWin(board, userChoice):
	print("")
	# TODO COMPLETE 
	

def main():
	board = Board()
	board.createBoard()	
	count = 0 # Used to keep track of whose turn it is
	while True:
		#board.tprintb()
		userChoice = makeMove(count%2)
		try: 
			userChoice = int(userChoice)
		except:
			break # Only way to get here is through typing exit
		checkMax = board.chosenMove(userChoice, count%2)
		if checkMax == SUCCESS:
			board.drawBoard()
			count +=1
		else:
			print("The maximum number of tiles in that row has been reach try again")
	print("A player has chosen to quit")

main()
	
	