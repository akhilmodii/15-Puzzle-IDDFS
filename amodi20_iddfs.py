import os
import time
from collections import deque

import itertools

import psutil


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.middle1 = None
        self.middle2 = None
        self.data = value
        self.parent = None
        self.action = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        # if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if node.data == data:
            return node
        elif node.left == None:
            node.left = self.insert(node.left, data)
        elif node.right == None:
            node.right = self.insert(node.right, data)
        elif node.middle1 == None:
            node.middle1 = self.insert(node.middle1, data)
        else:
            node.middle2 = self.insert(node.middle2, data)

        return node


# Method tp check if two lists are equal.
def checkEQ(list1, list2):
    if list1 == list2:
        return True
    else:
        return False


movesList = []  # Empty List. Will contain all the moves made to reach the solution.
moveValue = ''


# Method to evaluate moves made.
def moves(input):
    list = []
    boardList = eval(input)
    x = 0
    while 0 not in boardList[x]:
        x = x + 1
    y = boardList[x].index(0)

    if x > 0:  # Shifting UP
        boardList[x][y], boardList[x - 1][y] = boardList[x - 1][y], boardList[x][y]
        list.append(str(boardList))
        movesList.append('U')
        # moveValue = 'U'
        boardList[x][y], boardList[x - 1][y] = boardList[x - 1][y], boardList[x][y]

    if x < 3:  # Shifting DOWN
        boardList[x][y], boardList[x + 1][y] = boardList[x + 1][y], boardList[x][y]
        list.append(str(boardList))
        movesList.append('D')
        # moveValue = 'D'
        boardList[x][y], boardList[x + 1][y] = boardList[x + 1][y], boardList[x][y]

    if y > 0:  # Shifting LEFT
        boardList[x][y], boardList[x][y - 1] = boardList[x][y - 1], boardList[x][y]
        list.append(str(boardList))
        movesList.append('L')
        # moveValue = 'L'
        boardList[x][y], boardList[x][y - 1] = boardList[x][y - 1], boardList[x][y]

    if y < 3:  # Shifting RIGHT
        boardList[x][y], boardList[x][y + 1] = boardList[x][y + 1], boardList[x][y]
        list.append(str(boardList))
        movesList.append('R')
        # moveValue = 'R'
        boardList[x][y], boardList[x][y + 1] = boardList[x][y + 1], boardList[x][y]

    return list


def findPath(node):
    path = []
    while(node.parent is not None):
        path.append(node.action)
        node = node.parent
    path.reverse()
    return path



def IDDFS(initial, final, root):

    def dfs(route, depth):
        if depth == 0:
            return
        if route[-1] == final:
            return route
        for move in moves(route[-1]):
            if move not in route:
                nextRoute = dfs(route + [move], depth-1)
                if nextRoute:
                    return nextRoute

    for depth in itertools.count():
        route = dfs([root.data], depth)
        if route:
            # return route     # add find_path here
            return findPath(root)



# Formats the user input.
def inputFormat(userInput):
    newList = []
    userInput = userInput.replace(" ", ",")
    newUserInput = [str(k) for k in userInput.split(',')]
    newUserInput = list(map(int, newUserInput))
    for i in range(0, len(newUserInput), 4):
        newList.append(newUserInput[i:i + 4])
    return newList


# printing all the moves made to reach the solution.
def printMoves(list):
    for i in range(len(list)):
        print(list[i], end="")
    print('\n')


if __name__ == "__main__":
    # Tree.mtree = Tree.Tree()
    m = Tree()


    Tree.root = None
    root = Tree.root
    userInput = input("Enter initial configuration: ")
    startTime = time.time()
    process = psutil.Process(os.getpid())
    initialMemory = process.memory_info().rss / 1024.0
    newList = inputFormat(userInput)
    initialBoard = str(newList)
    finalBoard = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

    root = m.insert(root, initialBoard)
    # print(IDDFS(initialBoard, finalBoard, root))
    result = IDDFS(initialBoard, finalBoard, root)
    print(result)
    # BFS(initialBoard, finalBoard)
    # printMoves(movesList)
    finalMemory = process.memory_info().rss / 1024.0
    totalMemory = finalMemory - initialMemory
    endTime = time.time()
    totalTime = endTime - startTime
    print('Time taken: ' + str(totalTime))
    print('Total Memory used: ' + str(finalMemory) + ' KB')

"""
Inputs: 
1 0 3 4 5 2 6 8 9 10 7 11 13 14 15 12   

1 2 3 4 5 6 8 0 9 11 7 12 13 10 14 15

1 0 2 4 5 7 3 8 9 6 11 12 13 10 14 15

1 2 0 4 6 7 3 8 5 9 10 12 13 14 11 15 

1 3 4 8 5 2 0 6 9 10 7 11 13 14 15 12

"""
