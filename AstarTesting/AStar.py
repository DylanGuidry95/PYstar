'''Astar.py'''
from AstarTest import UnitTest
from vector import Vector2

def getneighbors(node, graph):
    '''Gets all the neighbors of this node in the graph passed in'''
    neighbors = []
    validpositions = []
    validpositions.append(node.position + Vector2(1, 0)) #Right
    validpositions.append(node.position + Vector2(1, 1)) #TopRight
    validpositions.append(node.position + Vector2(0, 1)) #Top
    validpositions.append(node.position + Vector2(-1, 1)) #TopLeft
    validpositions.append(node.position + Vector2(-1, 0)) #Left
    validpositions.append(node.position + Vector2(-1, -1)) #BotLeft
    validpositions.append(node.position + Vector2(0, -1)) #Bot
    validpositions.append(node.position + Vector2(1, -1)) #BotRight
    for node in graph.nodes:
        for position in validpositions:
            if node.position == position:
                neighbors.append(node)
    return neighbors

def calcgscore(node, currentnode, inlist):
    '''Calculates the gscore for the node based on the position of the node passed in'''
    tentativeg = 0
    if (node.position.xpos == currentnode.position.xpos or
            node.position.ypos == currentnode.position.ypos):
        tentativeg = 10
    else:
        tentativeg = 14
    if not inlist:
        node.gscore = currentnode.gscore + tentativeg
        node.parent = currentnode
    else:
        if node.gscore > tentativeg:
            node.gscore = currentnode.gscore + tentativeg
            node.parent = currentnode

def calchscore(node, goalnode):
    '''Calculates the manhatan distance from this node to the node passed in'''
    node.hscore = 10 * (abs(node.position.xpos - goalnode.position.xpos) +
                        abs(node.position.ypos - goalnode.position.ypos))

def calcfscore(node):
    '''Calculates the fscore for the current node'''
    node.fscore = node.gscore + node.hscore

def retrace(goal):
    '''Retraces the path from the goal node to the start node
    by following the node parents and returns a list of all nodes
    travered'''
    current = goal
    path = []
    while current is not None:
        path.append(current)
        current = current.parent
    return path

def algorithm(start, goal, graph):
    '''AStar algorithm implementation'''
    openlist = []
    closelist = []
    if start is None or goal is None:
        return [None]
    current = start
    openlist.append(current)
    while len(openlist) > 0:
        if start == goal:
            return [start]
        openlist.remove(current)
        closelist.append(current)
        neighbors = getneighbors(current, graph)
        for node in neighbors:
            if node not in openlist:
                if node not in closelist:
                    if node.iswalkable:
                        openlist.append(node)
                        calcgscore(node, current, False)
            else:
                if node not in closelist:
                    calcgscore(node, current, True)
            calchscore(node, goal)
            calcfscore(node)
        openlist.sort(key=lambda node: node.fscore)
        current = openlist[0]
        if goal in closelist:
            return retrace(goal)
    return None


TESTER = UnitTest("test.txt")
RESULTS = TESTER.testastar(algorithm)
