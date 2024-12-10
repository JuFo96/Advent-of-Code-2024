# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:04:42 2024

@author: Julius
"""

with open("input.txt", "r") as f:
    lines = f.readlines()

# Double list comprehension to convert list of strings to lists of lists of integers
data = [[int(element) for element in line.split()] for line in lines]


def window(data):
    condition1All = []
    condition2All = []
    result = []
    for row in data:
        first = True
        condition1 = []
        condition2 = []
        for i, element in enumerate(row):
            if first == True:
                first = False
                continue
            condition1.append(row[i] < row[i-1])
            condition2.append(abs(row[i] - row[i-1])
                              < 4 and abs(row[i] - row[i-1]) > 0)
        condition1All = all([x == True for x in condition1]) or all(
            [x == False for x in condition1])
        condition2All = all(condition2)
        result.append(condition1All and condition2All)
    return result


def checkConditions(row):
    first = True
    condition1 = []
    condition2 = []
    for i, element in enumerate(row):
        if first == True:
            first = False
            continue
        condition1.append(row[i] < row[i-1])
        condition2.append(abs(row[i] - row[i-1])
                          < 4 and abs(row[i] - row[i-1]) > 0)
    return condition1, condition2


dummy = window(data)
print(sum(dummy))


def window2(data):
    condition1All = []
    condition2All = []
    result = []
    for row in data:
        first = True
        condition1 = []
        condition2 = []
        for i, element in enumerate(row):
            if first == True:
                first = False
                continue
            condition1.append(row[i] < row[i-1])
            condition2.append(abs(row[i] - row[i-1])
                              < 4 and abs(row[i] - row[i-1]) > 0)
        condition1All = all([x == True for x in condition1]) or all(
            [x == False for x in condition1])
        condition2All = all(condition2)
        result.append(condition1All and condition2All)
    return result
