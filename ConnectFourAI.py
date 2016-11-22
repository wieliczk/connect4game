import main


#every nodename is a key to node object.


class Node:
    def __init__(self):
        self.name = "null"
        self.board = None
        self.children = []
        self.parents = []
        self.negamax = None

    def defineNode(self, boardconfig, parentsP, negaMax, childrenP=None):
        self.name = self
        self.board = boardconfig
        self.children = [childrenP]
        self.parents = [parentsP]
        self.negamax = negaMax

    def gotoChild(self,childIndex):
        return self.children[int(childIndex)]

    def addChild(self, childNode):
        self.children.append(childNode)

    def newChildNode(self, name, board):
        name = name.Node()
        name.defineNode(board, self, -999)

    def gotoParent(self, parentIndex):
        return self.parents[int(parentIndex)]

    def addParent(self, parentNode):
        self.parents.append(parentNode)

    def getNegaMax(self):
        return self.negamax

    def negaMaxAss(self, newNegamax):
        self.negamax = newNegamax

    def getBoard(self):
        return self.board




#GameTree Builder Code

gameTree = []

#Sorts all nodenames in the same depth into a list, from 0 to 41.

depthList = []

#alpha/beta values will be assigned at beginning of game.

alpha = None
beta =  None
_0V0 = Node()
_0V0.defineNode([[],[],[],[],[],[],[],[]], -999, [])
GameTree = [_0V0]
nameCounter = 0
depthList= [[]]


#returns a boolean value of weather a board already has a symmetrical
copy
def breadthSymCheck(self, board, depth):
    symBoard = board.reverse()
    for node in depthList[depth]:
        if node.board == symBoard:
            return True
        else:
            return False

#returns a boolean value of weather a node with the board already exists in the depth
def breadthChildCheck(self, board, depth):
    for node in depthList[depth]:
        if node.board == board:
            return node
            break
        else:
            return None

    
        

#Depth-first node generation

def depthCheck(node):
    for number in node.name:
        if number == "V":
            depth = int(node.name[number + 1])
            try:
                depth = (depth*10) + int(node.name[number + 2])
                return depth
            except:
                return depth
    
    

def TreeGen(node, index=0):
    #Create board of next possible node via chosenMove()
    #If there are nodes already, compare the board to the boards of each node.
    #If board is not symmetric or equal to boards already in depth level,
    #create child Node with the board, with a name as (nameCounter)_(Depth)
    #Loop this until win/loss/tie found
    #check if it is a winner/loser/tie, and if so , assign child node negaMax
    #100/-100/0, & update alpha and beta. assign negaMax to all parents leading
    #to that node, and continue going up until the parent node has the potential
    #for new children (unexplored moves)
    #when the generation finally returns to top after all is done, print out
    #GameTree List
    depth = depthCheck(node)
    posBoard = board.chosenMove(index,(depth % 2))
    depth = depthCheck(node)

    #checks if it is a leaf node and if so , assigns a negamax.
    if node.name != "_0V0":
        winLoss = checkWin(posBoard,index)
        if winLoss == 1:
            node.negaMaxAss(100)
        if winLoss == 0:
            node.negaMaxAss(-100)
        if depthCheck(node) == 42:
            node.negaMaxAss(0)



    if breadthSymCheck(posBoard, depth) == True and index < 6:
        TreeGen(node, index + 1)
        
    sharedChild = breadthChildCheck(posBoard, depth)

    if sharedChild != None:
        sharedChild.addParent(node)
        TreeGen(node, index + 1)

    #the board is unique and thus the node is created.
    TreeGen(node.newChildNode("_" + str(nameCounter) + 'V' + str(depth + 1)), posBoard)
        
    
    
    
    



    
    
    
      









    


 
        
        

        
        

        
        




