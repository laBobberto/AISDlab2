import numpy as np
import json

from Trees.RBTree import RedBlackTree
from constants import heights


def orderProcessing(orderResult, olnyNums = True):
    result = []
    if olnyNums:
        for i in orderResult:
            result.append(i[0])
    else:
        for i in orderResult:
            result.append(str(i[0]) + "b" if i[1]=="black" else "r")
    return result

def generateResult(trees_func, heights):
    allCases = []

    for i in trees_func:
        worstCaseResult = []
        avCaseResult = []
        bestCaseResult = []

        print(heights)
        for j in heights:
            worstTree = i()
            avTree = i()
            bestTree = i()
            keys = [k for k in range(j)]

            worstTree.worstInsert(keys)
            avTree.averageInsert(keys)
            bestTree.bestInsert(keys)

            worstCaseResult.append([j, worstTree.getHeight(worstTree.root)])
            avCaseResult.append([j, avTree.getHeight(avTree.root)])
            bestCaseResult.append([j, bestTree.getHeight(bestTree.root)])
            print(j)

        allCases.append(worstCaseResult)
        allCases.append(avCaseResult)
        allCases.append(bestCaseResult)

    return allCases


def writeArrays(filename, arrays):
    if len(arrays) != 9:
        raise ValueError("Ожидается 9 двумерных массивов или списков.")
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(arrays, file)


def readArrays(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        arrays_as_lists = json.load(file)

    arrays = [array for array in arrays_as_lists]
    result = []
    [result.append([arrays[i*3], arrays[i*3+1], arrays[i*3+2]]) for i in range(len(arrays)//3)]

    return result

def fixData():
    correctData = [[], [], []]
    for i in heights:
        worst = RedBlackTree()
        average = RedBlackTree()
        best = RedBlackTree()

        keys = [x for x in range(i)]

        worst.worstInsert(keys)
        average.averageInsert(keys)
        best.bestInsert(keys)
        correctData[0].append([i,worst.getHeight(worst.root)])
        correctData[1].append([i,average.getHeight(average.root)])
        correctData[2].append([i,best.getHeight(best.root)])
        # print(f"\n{i}")
        # print(worst.getHeight(worst.root))
        # print(average.getHeight(average.root))
        # print(best.getHeight(best.root))
    return correctData
