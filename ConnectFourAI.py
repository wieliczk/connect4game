from main import Board
from main import checkWin
from copy import deepcopy

#every nodename is a key to node object.


class Node:
    def __init__(self):
        self.name = "null"
        self.board = None
        self.children = []
        self.parents = []
        self.negamax = None
        self.depth = 0
        #self.visits = []

    def defineNode(self, name, boardconfig, parentsP, negaMax, depth=0, childrenP=[]):
        self.name = name
        self.board = boardconfig
        self.children = [childrenP]
        self.parents = [parentsP]
        self.negamax = negaMax
        self.depth = depth
        #self.visits = []

    def getNodeName(self):
        return self.name

    def gotoChild(self,childIndex):
        return self.children[int(childIndex)]

    def addChild(self, childNode):
        self.children.append(childNode)

    def newChildNode(self, childName, board):
        node = Node()
        parent = self.getNodeName()
        node.defineNode(childName, board, parent, -999, self.getDepth() + 1)
        return node

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

    def getDepth(self):
        return self.depth

    #def getVisits(self):
        #return self.visits

    #def addVisits(visit):
        #self.visits.append(visit)



#GameTree Builder Code
#Sorts all nodenames in the same depth into a list, from 0 to 41.
#alpha/beta values will be assigned at beginning of game.
#returns a boolean value of weather a board already has a symmetrical
#copy
def breadthSymCheck(inBoard, depth):
    global depthList
    symBoard = deepcopy(inBoard)
    symBoard.bRows.reverse()
    for node in depthList[depth]:
        if node.getBoard().bRows == symBoard.bRows:
            return True
    return False

#returns a boolean value of weather a node with the board already exists in the depth
def breadthChildCheck(board, depth):
    global depthList
    for node in depthList[depth]:
        if node.getBoard() == board:
            return node
    return None
            
        

def labelCheck(node):
    name = node.getNodeName()
    return int(name[1:])
        
            


print("-----------treeGen---------")


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
    
global alpha
alpha = None
global beta
beta =  None
_0 = Node()
board = Board()
board.createBoard()
#print(board)
_0.defineNode("_0", board, -999, [])
#print(_0.getBoard())
global gameTree
gameTree= [_0]
global depthList
depthList = [[]]
global labelCounter
labelCounter = 0

def treeGen(node, index):
    global labelCounter
    global depthList
    #checks if it the current node is a leaf node
    #and if so , assigns a negamax.
    depth = node.getDepth()
          

    print("---NODE start")
    #print(node)
    print(node.getNodeName())
    print(depth)
    newBoard = deepcopy(node.getBoard())
    #checks if the column is full 
    print("index length: " + str(len(newBoard.bRows[index])))
    if len(newBoard.bRows[index]) >= 6:
        for column in range(0, 7):
            if len(newBoard.bRows[column]) < 6 and (column != index):
                newBoard.chosenMove(column, depth%2)
                index = column
                break
    else:
        newBoard.chosenMove(index, depth%2)
    print("Current Node Board: " + str(node.getBoard().bRows))
    print("new index length: " + str(len(newBoard.bRows[index])))
    #print(board.bRows)
    print("index:" + str(index))
    print(newBoard.bRows)

    




    #Symmetry and multichild checks
    print("symmetry check!")
    if breadthSymCheck(newBoard, depth):
        print("FOUND SYMMETRY")
        treeGen(node, index + 2)
        
    
    elif breadthChildCheck(newBoard, depth) != None:
        print("FOUND SHARED CHILD")
        sharedChild.addParent(node)
        treeGen(node, index + 2)
        
        #print("shared check")

    #the board is unique and thus the node is created.
    else:
        labelCounter += 1
        child = node.newChildNode(str("_" + str(labelCounter)), newBoard)
        if len(depthList) - 1 < child.getDepth():
            depthList.append([])
        depthList[child.getDepth()].append(child)
    
        winLoss = checkWin(child.getBoard(),index)
        print("child depth: " + str(child.getDepth()))
        print("---Node end")
        print("Check for WIN!")
        if winLoss == 1:
            if (depth)%2 == 0: #Even depths are player 1 turns
                child.negaMaxAss(100)
                #treeGen(child, index + 1)
                for x in range(0, 10):
                    print("WIN")
                    print(child.getNodeName())
            else:
                child.negaMaxAss(-100)
                for x in range(0, 10):
                    print("LOSE")
                #treeGen(child, index + 1)
        elif depth >= 42:
            child.negaMaxAss(0)
            for x in range(0, 10):
                    print("TIE")
        else:
            treeGen(child, index)
            print("RETURN TO PARENT")
            try:
                treeGen(child, index + 2)
            except:
                print()
    
            
                

 
treeGen(_0, 0)


    
    
    



    
    
    
      









    


 
        
        

        
        

        
        




