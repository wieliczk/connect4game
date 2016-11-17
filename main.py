import sys
""" Main game for Connect Four game
	Game Requires no input as it is 8 long and 8 high"""

MAXHEIGHT = 8
MAXROW = 8
ACCEPTED = [0,1,2,3,4,5,6,7]
QUITS = "exit"

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
		if player == 0:
			self.bRows[choice].append("x")
		else:
			self.bRows[choice].append("o")
	
	# For testing
	def tprintb(self):
		print(self.bRows)

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

def main():
	board = Board()
	board.createBoard()	
	count = 0 # Used to keep track of whose turn it is
	while True:
		board.tprintb()
		userChoice = makeMove(count%2)
		try: 
			userChoice = int(userChoice)
		except:
			break # Only way to get here is through typing exit
		board.chosenMove(userChoice, count%2)
		count +=1
	print("A player has chosen to quit")

main()
	
	