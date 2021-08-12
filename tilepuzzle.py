## tilepuzzle.py
#Parminder Singh
# up down left right move generations



#notes
# for count, value in enumerate(values):
#     print(count, value)

# 1)The count of the current iteration
# 2) The value of the item at the current iteration



#test cases
# tilepuzzle([[2,8,3],[1,0,4],[7,6,5]],[[1,2,3],[8,0,4],[7,6,5]], 8)

import copy #for deepcopy function
import sys  #for setrecursionlimit function

def tilepuzzle(start, goal,recursionLimit):
    return reverse(statesearch([start], goal, [],recursionLimit))  #shows all of the moves

def statesearch(unexplored, goal, path,recursionLimit):

    if unexplored == []: #if empty return empty
        return []
    elif recursionLimit == 0: #if recursion limit is 0 return list
        return []
    elif goal == head(unexplored):  #need explanation from OH
        return cons(goal, path)
    elif len(path) == recursionLimit:   #backtracking depth limit
        return statesearch(tail(unexplored), goal, path,recursionLimit)
    elif head(unexplored) in path:
        unexplored.remove(head(unexplored))
        return statesearch(unexplored, goal, path,recursionLimit)
    else:
        result = statesearch(generateNewStates(head(unexplored)),
                         goal,
                         cons(head(unexplored), path),recursionLimit)

        if result != []:
            return result
        else:
            return statesearch(tail(unexplored),
                               goal,
                               path,recursionLimit)

def up(currState):
    result  = []
    tempState = copy.deepcopy(currState)

    if 0 in currState[0]:  #if there is a 0 in the top row, you cant go up so you just return result
        return result


#i is row j is column (and state is the actual j value in the tile)
    for i, lst in enumerate(currState):
        for j, state in enumerate(lst):
            if state == 0:
                tempState[i][j], tempState[i - 1][j] = tempState[i - 1][j], tempState[i][j]
                result.append(tempState)

    return result

def down(currState):  #if there is a 0 in the bottom row, you cant go up so you just return result
    result = []
    tempState = copy.deepcopy(currState)

    if 0 in currState[2]:
        return result

    for i, lst in enumerate(currState):
        for j, state in enumerate(lst):
            if state == 0:
                tempState[i][j], tempState[i + 1][j] = tempState[i + 1][j], tempState[i][j]
                result.append(tempState)

    return result

def left(currState):
    result = []
    tempState = copy.deepcopy(currState)

    for sublist in currState:
        if sublist[0] == 0: # ''
            return result

    for i, lst in enumerate(currState):
        for j, state in enumerate(lst):
            if state == 0:
                tempState[i][j], tempState[i][j - 1] = tempState[i][j - 1], tempState[i][j]
                result.append(tempState)

    return result


def right(currState):
    result = []
    tempState = copy.deepcopy(currState)

    for sublist in currState:
        if sublist[2] == 0: # ''
            return result

    for i, lst in enumerate(currState):
        for j, state in enumerate(lst):
            if state == 0:
                tempState[i][j], tempState[i][j+1] = tempState[i][j+1], tempState[i][j]
                result.append(tempState)

    return result

def reverseEach(listOfLists):
    result = []
    for st in listOfLists:
        result.append(reverse(st))
    return result


#helper functions

def reverse(st):
    return st[::-1]


def head(lst):
    return lst[0]


def tail(lst):
    return lst[1:]


def take(n, lst):
    return lst[0:n]


def drop(n, lst):
    return lst[n:]


def cons(item, lst):
    return [item] + lst


def generateNewStates(currState):
    return (up(currState) + down(currState) +
            right(currState) + left(currState))
