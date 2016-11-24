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

    def defineNode(self, name, boardconfig, parentsP, negaMax, depth=0, childrenP=[]):
        self.name = name
        self.board = boardconfig
        self.children = [childrenP]
        self.parents = [parentsP]
        self.negamax = negaMax
        self.depth = depth

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



#GameTree Builder Code
#Sorts all nodenames in the same depth into a list, from 0 to 41.
#alpha/beta values will be assigned at beginning of game.
#returns a boolean value of weather a board already has a symmetrical
#copy
def breadthSymCheck(inBoard, depth):
    symBoard = deepcopy(inBoard)
    symBoard.bRows.reverse()
    for node in depthList[depth]:
        if node.board.bRows == symBoard.bRows:
            return True
        else:
            return False

#returns a boolean value of weather a node with the board already exists in the depth
def breadthChildCheck(board, depth):
    for node in depthList[depth]:
        if node.board == board:
            return node
            break
        else:
            return None
        


#def depthCheck(node):
#    name = node.getNodeName()
#    print(name)
#    count = 0
 #   for number in name:
  #      if number == "V":
   #         depth = int(name[count + 1])
    #        try:
     #           depth = (depth*10) + int(name[count + 2])
      #          return depth
       #     except:
        #        return depth
        #count = count + 1

def labelCheck(node):
    name = node.getNodeName()
    return int(name[1:])
        
            
        
    
alpha = None
beta =  None
_0 = Node()
board = Board()
board.createBoard()
#print(board)
_0.defineNode("_0", board, -999, [])
#print(_0.getBoard())
GameTree = [_0]
depthList= [[]]

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
def treeGen(node, index):
    print("NODE start")
    #print(node)
    print(node.getNodeName())
    depth = node.getDepth()
    print(depth)
    board = node.getBoard()
    newBoard = deepcopy(board)
    newBoard.chosenMove(index, depth%2)
    print(board.bRows)
    print(newBoard.bRows)
    

    #checks if it is a leaf node and if so , assigns a negamax.
    if node.name != "_0":
        winLoss = checkWin(board, index)
        if winLoss == 1:
            node.negaMaxAss(100)
        elif winLoss == 0:
            node.negaMaxAss(-100)
        elif depth == 42:
            node.negaMaxAss(0)



    #if breadthSymCheck(board, depth) and index < 6:
      #  board.bRows
       # treeGen(node, index + 1
       #print("Sym Check")
        
    #sharedChild = breadthChildCheck(board, depth)

    #if sharedChild != None:
        #sharedChild.addParent(node)
        #treeGen(node, index + 1)
        #print("shared check")

    #the board is unique and thus the node is created.
   
    label = labelCheck(node)
    label = str(label + 1)
    child = node.newChildNode(str("_" + label), newBoard)
    print("Node end")

    if len(depthList) - 1 < child.getDepth():
        depthList.append([])
    depthList[child.getDepth()].append(child)
    #print(newBoard.bRows)
    treeGen(child, index)

 
treeGen(_0, 0)


    
    
    



    
    
    
      









    


 
        
        

        
        

        
        




