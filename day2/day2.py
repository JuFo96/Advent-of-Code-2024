# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:11:16 2024

@author: Julius
"""
# https://adventofcode.com/2024/day/2

with open("input.txt", "r") as f:
    lines = f.readlines()

# Double list comprehension to convert list of strings to lists of lists of integers
data = [[int(element) for element in line.split()] for line in lines]


def evaluateAdjacentChanges(report):
    adjacencyList = []
    for i in range(len(report)-1):
        adjacencyList.append(report[i] - report[i+1])
    return adjacencyList


def condition1(adjacencyList):
    if all(x < 0 for x in adjacencyList) or all(x > 0 for x in adjacencyList):
        return True


def condition2(adjacencyList):
    if all([abs(x) > 0 and abs(x) < 4 for x in adjacencyList]):
        return True


def testcon(adjacencyList):
    lil = [abs(x) > 0 and abs(x) < 4 for x in adjacencyList]
    return lil


def evaluateReports(adjacencyList):
    if condition1(adjacencyList) and condition2(adjacencyList):
        return True
    return False


def evaluateReports2(adjacencyList):
    if (sum(x < 0 for x in adjacencyList) > len(adjacencyList)-2 or sum(x > 0 for x in adjacencyList) > len(adjacencyList)-2) and sum([abs(x) > 0 and abs(x) < 4 for x in adjacencyList]) > len(adjacencyList)-2:
        # Report is safe
        return True
    return False


def extractIndex(adjacencyList):
    for i, booleanIndex in enumerate(adjacencyList):
        if booleanIndex == False:
            return i
    return None


def removeIndex(adjacencyList, index):
    del adjacencyList[index]
    return adjacencyList


def updateData(data):
    for row in data:
        adjacencyList = testcon(evaluateAdjacentChanges(row))
        idx = extractIndex(adjacencyList)
        if idx != None:
            removeIndex(row, idx)


# updateData(data)
counter = 0
for i in range(len(data)):
    if evaluateReports(evaluateAdjacentChanges(data[i])) == True:
        counter += 1


print(counter)
updateData(data)
testD = evaluateAdjacentChanges(data[12])
boolTest = testcon(testD)
