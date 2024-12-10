# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:12:38 2024

@author: Julius
"""

pageMap = []
pageOrder = []

with open("test.txt", "r") as f:
    for line in f:
        pageOrder.append(line)
        if line == "\n":
            pageMap = pageOrder
            pageOrder = []
            del pageMap[-1]


numberList1 = []
numberList2 = []
pageDict = {}

for row in pageMap:
    numberList1.append(int(row[:2]))
    numberList2.append(int(row[3:5]))
    key = int(row[:2])
    value = int(row[3:5])
    pageDict.update({key: value})


testSet1 = set(numberList1)
testSet2 = set(numberList2)
