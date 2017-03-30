#pylint rate: 10/10
'''File that handles the testing of the astar algorithm'''
from AStar import AStarAlgorithm
from AStar import Graph
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

def getcorrectpath(testcase):
    '''Gets the desierd result of the current test case from the string'''
    path = open("test.txt", "r")
    vectors = []
    for line in path:
        if "#" in line:
            continue
        if testcase + "=answer=" in line:
            for i in range(0, len(line)):
                value = ""
                if line[i] == '[':
                    i = i + 1
                    while line[i] != ']':
                        value = value + line[i]
                        i = i + 1
                    vectors.append(value)
    return vectors

def setupastar(enviorment, algorithm):
    '''Sets up the enviorment currently being tested based on the
    contents of the string passed in by enviorment'''
    for iterator in range(0, len(enviorment)):
        if enviorment[iterator] == 'G':
            iterator = iterator + 2
            nodevalue = ""
            while enviorment[iterator] != ';':
                nodevalue = nodevalue + enviorment[iterator]
                iterator = iterator + 1
            algorithm.setgoal(algorithm.graph.getnode(nodevalue))
        if enviorment[iterator] == 'S':
            iterator = iterator + 2
            nodevalue = ""
            while enviorment[iterator] != ';':
                nodevalue = nodevalue + enviorment[iterator]
                iterator = iterator + 1
            algorithm.setstart(algorithm.graph.getnode(nodevalue))
        if enviorment[iterator] == 'W':
            iterator = iterator + 2
            nodevalue = ""
            while enviorment[iterator] != ';':
                nodevalue = nodevalue + enviorment[iterator]
                iterator = iterator + 1
            algorithm.graph.getnode(nodevalue).iswalkable = False

def setuptestcases():
    '''Iterates through the the files designated for testing the functionality
    of AStar. Invokes setupastar, testastar function, and getcorrectpath.'''
    enviorment = open("test.txt")
    lines = enviorment.readlines()
    answer = open("answer.txt", "w").close()
    testnum = 0
    answer = open("answer.txt", "a")
    for line in lines:
        if "#" in line:
            continue
        if "==>" in line:
            testnum = testnum + 1
            algo = AStarAlgorithm(Graph(10, 10)) #replace with astar object we are testing
            setupastar(line, algo)
            answer.write(line)
            answer.write("Test" + str(testnum) + "=ReturnPath=")
            testastar(algo.algorithm(), "Test" + str(testnum), answer)
    answer.close()

def testastar(userpath, testid, answerfile):
    '''Userpath is the path returned by the astar algorithm
    Correctpath is a string representation of a correct path
    answerfile is the file we will write the path of the algorithm
    Test the value of astar'''
    correctpath = getcorrectpath(testid)
    numcorrect = 0
    if userpath is not None:
        for node in range(0, len(userpath)):
            if str(userpath[node].value) == correctpath[node]:
                numcorrect = numcorrect + 1
            answerfile.write("[" + str(userpath[node].value) + "]")
    answerfile.write('\n')
    correctpercent = (float(numcorrect) / float(len(correctpath))) * 100
    answerfile.write(str(testid) + "===answer===")
    for value in correctpath:
        answerfile.write("[" + value + "]")
    answerfile.write('\n')
    answerfile.write("Correct:" + str(correctpercent))
    answerfile.write('\n')
    answerfile.write('\n')

setuptestcases()
