'''Astar.py'''
from AstarTest import UnitTest

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
        neighbors = current.getneighbors(graph)
        for node in neighbors:
            if node not in openlist:
                if node not in closelist:
                    if node.iswalkable:
                        openlist.append(node)
                        node.calcgscore(current, False)
            else:
                if node not in closelist:
                    node.calcgscore(current, True)
            node.calchscore(goal)
            node.calcfscore()
        openlist.sort(key=lambda node: node.fscore)
        current = openlist[0]
        if goal in closelist:
            return retrace(goal)
    return None


test = UnitTest("test.txt")
test.gentestcases()
a = test.testastar(algorithm)
