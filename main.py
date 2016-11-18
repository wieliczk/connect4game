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
		for i in range(40):
			print("") # Clean up above board
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
		
	def returnBoard(self):
		aList = self.bRows
		return aList
		
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
	checks = 1
	boardList = board.returnBoard()
	usertile = boardList[userChoice][-1] # Gets the last added tile in list
	level = len(boardList[userChoice])-1
	while True:
		if checks == 1:
			countWin = 1
			countWin = checkRight(boardList, usertile, userChoice, level, countWin)
			if countWin == 4:
				return SUCCESS
			else:
				countWin = checkLeft(boardList, usertile, userChoice, level, countWin)
				if countWin == 4:
					return SUCCESS
				else:
					checks = 2
		if checks == 2:
			countWin = 1
			countWin = checkDown(boardList, usertile, userChoice, level, countWin)
			if countWin == 4:
				return SUCCESS
			else:
				checks = 3
		if checks == 3:
			countWin = 1
			countWin = checkdagRU(boardList, usertile, userChoice, level, countWin)
			if countWin == 4:
				return SUCCESS
			else:
				countWin = checkdagLD(boardList, usertile, userChoice, level, countWin)
				if countWin == 4:
					return SUCCESS
				else:
					checks = 4
		if checks == 4:
			countWin = 1
			countWin = checkdagLU(boardList, usertile, userChoice, level, countWin)
			if countWin == 4:
				return SUCCESS
			else:
				countWin = checkdagRD(boardList, usertile, userChoice, level, countWin)
				if countWin == 4:
					return SUCCESS
				else:
					return FAIL 
				
			
	# TODO COMPLETE 
	
def checkRight(aList, tile, row, level, count):
	try:
		if aList[row+1][level] == tile:
			count += 1
			row += 1
			if row >= MAXROW: # Border checking
				raise Exception 
			if count == 4:
				raise Exception
			count = checkRight(aList, tile, row, level, count)
		else:
			return int(count)
	except:
		return int(count) 
	return count

def checkLeft(aList, tile, row, level, count):
	try:
		if aList[row-1][level] == tile:
			count +=1
			row -=1
			if row <= 0: # Border checking
				row = LIMIT
			if count == 4:
				raise Exception
			count = checkLeft(aList, tile, row, level, count) 
		else:
			return count
	except:
		return count
	return count

# Never need to check up because starting at highest position possible
def checkDown(aList, tile, row, level, count):
	try:
		if aList[row][level-1] == tile:
			count +=1
			level -=1
			if level <= 0: 
				raise Exception
			elif level >= MAXHEIGHT:
				raise Exception
			if count == 4:
				raise Exception
			count = checkDown(aList, tile, row, level, count)
		else:
			return count
	except:
		return count
	return count

# Checks diagonal right up 	 
def checkdagRU(aList, tile, row, level, count):
	try:
		if aList[row+1][level+1] == tile:
			count +=1
			row +=1
			level +=1
			if level >= MAXHEIGHT: # Only have to check upper limit
				raise Exception
			elif row >= MAXROW:
				raise Exception
			elif count == 4: 
				raise Exception
			else:
				count = checkdagRU(aList, tile, row, level, count)
		else:
			return count
	except:
		return count
	return count 
	
# Checks diagonal left up
def checkdagLU(aList, tile, row, level, count):
	try:
		if aList[row-1][level+1] == tile:
			count +=1
			row -=1
			level +=1
			if level >= MAXHEIGHT:
				raise Exception
			elif row <= 0:
				raise Exception
			elif count == 4:
				raise Exception
			else:
				count = checkdagLU(aList, tile, row, level, count)
		else:
			return count
	except:
		return count
	return count

# Checks diagonal right down
def checkdagRD(aList, tile, row, level, count):
	try: 
		if aList[row+1][level-1] == tile:
			count +=1
			row +=1
			level -=1
			if level <= 0:
				raise Exception
			elif row >= MAXROW:
				raise Exception
			elif count == 4:
				raise Exception
			else:
				count = checkdagRD(aList, tile, row, level, count)
		else:
			return count
	except:
		return count 
	return count

# Checks diagonal left down
def checkdagLD(aList, tile, row, level, count):
	try:
		if aList[row-1][level-1] == tile:
			count +=1
			row -=1
			level -=1
			if level <= 0: #Only have to check lower limit
				raise Exception
			elif row <= 0:
				raise Exception 
			elif count == 4:
				raise Exception
			else:
				count = checkdagLD(aList, tile, row, level, count) 
		else:
			return count 
	except:
		return count
	return count 
	

def main():
	# Incase somehow there is a tie 
	maxTurns = (MAXHEIGHT * MAXROW)
	winState = 0 
	board = Board()
	board.createBoard()	
	turn = 0 # Used to keep track of whose turn it is
	while turn != maxTurns:
		#board.tprintb()
		userChoice = makeMove(turn%2)
		try: 
			userChoice = int(userChoice)
		except:
			break # Only way to get here is through typing exit
		checkMax = board.chosenMove(userChoice, turn%2)
		if checkMax == SUCCESS:
			board.drawBoard()
			isWin = checkWin(board, userChoice)
			if isWin == SUCCESS:
				winState = 1
				break
			turn +=1
		else:
			print("The maximum number of tiles in that row has been reach try again")
	if winState == 1:
		if turn%2 == 0:
			print("Player 1 has won!")
		else:
			print("Player 2 has won!")
	elif maxTurns == turn:
		print("I honestly never thought it would get here... All tied up") 
	else:
		print("A player has chosen to quit")

main()
	
	