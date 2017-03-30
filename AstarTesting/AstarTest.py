#pylint rate: 10/10
'''File that handles the testing of the astar algorithm'''
#Usage documentation
#all nodes must have a value that is of type string and be numbered from
#0 - 99, where 0 = <0,0> 99 = <9, 9>
#Nodes must be able to be toggle as iswalkable
#The graph must have a way to get get a node from it based on the value we are searching for

#Required functions
#======================
#Graph -> getnode(nodevalue)
#algorithm -> setstart(node)
#algorithm -> setgoal(node)
#algorithm -> algorithm() //this will return a path in the form of a list of nodes
#algorithm -> must be able to store a refrence of a graph
import re
from vector import Vector2

class Graph(object):
    '''Graph'''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = []
        self.gengraph()

    def gengraph(self):
        '''generates the graph'''
        nodecount = 0
        for row in range(0, self.width):
            for col in range(0, self.height):
                self.nodes.append(Node(Vector2(col, row), str(nodecount)))
                nodecount = nodecount + 1

    def getnode(self, nodeval):
        '''Checks to see if a node with the nodevalue passed in is in the graph'''
        for node in self.nodes:
            if node.value == nodeval:
                return node
        return None

class Node(object):
    '''Node'''
    def __init__(self, position, value):
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0
        self.position = position
        self.parent = None
        self.value = value
        self.iswalkable = True

    def getneighbors(self, graph):
        '''Gets all the neighbors of this node in the graph passed in'''
        neighbors = []
        validpositions = []
        validpositions.append(self.position + Vector2(1, 0)) #Right
        validpositions.append(self.position + Vector2(1, 1)) #TopRight
        validpositions.append(self.position + Vector2(0, 1)) #Top
        validpositions.append(self.position + Vector2(-1, 1)) #TopLeft
        validpositions.append(self.position + Vector2(-1, 0)) #Left
        validpositions.append(self.position + Vector2(-1, -1)) #BotLeft
        validpositions.append(self.position + Vector2(0, -1)) #Bot
        validpositions.append(self.position + Vector2(1, -1)) #BotRight
        for node in graph.nodes:
            for position in validpositions:
                if node.position == position:
                    neighbors.append(node)
        return neighbors

    def calcgscore(self, node, inlist):
        '''Calculates the gscore for the node based on the position of the node passed in'''
        tentativeg = 0
        if self.position.xpos == node.position.xpos or self.position.ypos == node.position.ypos:
            tentativeg = 10
        else:
            tentativeg = 14
        if not inlist:
            self.gscore = node.gscore + tentativeg
            self.parent = node
        else:
            if self.gscore > tentativeg:
                self.gscore = node.gscore + tentativeg
                self.parent = node

    def calchscore(self, node):
        '''Calculates the manhatan distance from this node to the node passed in'''
        self.hscore = 10 * (abs(self.position.xpos - node.position.xpos) +
                            abs(self.position.ypos - node.position.ypos))

    def calcfscore(self):
        '''Calculates the fscore for the current node'''
        self.fscore = self.gscore + self.hscore

class TestCase(object):
    def __init__(self, name, case, answer):
        self.name = name
        self.name = re.sub('name:', '', self.name)
        self.case = case
        self.case = re.sub('case:', '', self.case)
        self.answer = answer
        self.answer = re.sub('answer:', '', self.answer)

    def setupgraph(self):
        graph = Graph(10, 10)
        for iterator in range(0, len(self.case)):
            if self.case[iterator] == 'W':
                iterator = iterator + 2
                nodevalue = ""
                while self.case[iterator] != ';':
                    nodevalue = nodevalue + self.case[iterator]
                    iterator = iterator + 1
                graph.getnode(nodevalue).iswalkable = False
        return graph

    def getstartandgoal(self):
        start = ""
        goal = ""
        for iterator in range(0, len(self.case)):
            if self.case[iterator] == 'G':
                iterator = iterator + 2
                nodevalue = ""
                while self.case[iterator] != ';':
                    nodevalue = nodevalue + self.case[iterator]
                    iterator = iterator + 1
                goal = nodevalue
            if self.case[iterator] == 'S':
                iterator = iterator + 2
                nodevalue = ""
                while self.case[iterator] != ';':
                    nodevalue = nodevalue + self.case[iterator]
                    iterator = iterator + 1
                start = nodevalue
        return (start, goal)

    def getcorrectpath(self):
        nodes = []
        for iterator in range(0, len(self.answer)):
            nodevalue = ""
            if self.answer[iterator] == '[':
                iterator = iterator + 1
                while self.answer[iterator] != ']':
                    nodevalue = nodevalue + self.answer[iterator]
                    iterator = iterator + 1
                nodes.append(nodevalue)
        return nodes


class UnitTest(object):
    def __init__(self, testcasefile):
        self.start = None
        self.goal = None
        self.result = [None]
        self.testfile = open(testcasefile, "r")
        self.testcases = []

    def gentestcases(self):
        '''abc'''
        linecount = 0
        lines = self.testfile.readlines()
        for line in lines:
            if "#" in line or line == '\n':
                linecount = linecount + 1
                continue
            if "{" in line:
                name = ""
                case = ""
                answer = ""
                while "}" not in lines[linecount]:
                    if "name:" in lines[linecount]:
                        name = lines[linecount]
                    elif "case:" in lines[linecount]:
                        case = lines[linecount]
                    elif "answer:" in lines[linecount]:
                        answer = lines[linecount]
                    linecount = linecount + 1
                self.testcases.append(TestCase(name, case, answer))

    def testastar(self, algorithm):
        tests = []
        for case in self.testcases:
            enviorment = case.setupgraph()
            points = case.getstartandgoal()
            self.start = enviorment.getnode(points[0])
            self.goal = enviorment.getnode(points[1])
            path = algorithm(self.start, self.goal, enviorment)
            correctanswer = case.getcorrectpath()
            for iterator in range(0, len(correctanswer)):
                if path[iterator].value != correctanswer[iterator]:
                    tests.append(False)
                    continue
            tests.append(True)
        return tests

