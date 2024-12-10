# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:45:12 2024

@author: Julius
"""

import numpy as np
import pandas as pd

data = np.loadtxt("input.txt")

# https://adventofcode.com/2024/day/1
# Objective is to match the largest number in column 0 with the largest number in column 1,
# find the difference between them and repeat for all rows, sum the differences and that is the solution.


def calculatePointwiseDistance(data):
    sortedData = np.sort(data, 0)
    pointwiseDistance = np.abs(sortedData[:, 0] - sortedData[:, 1])
    totalDistance = np.sum(pointwiseDistance)
    # print(
    #    f"The total distance of all pointwise objects is {totalDistance:.0f}")
    return totalDistance


def calculateSimilarityScore(data):
    colTwoUniqueCounts = pd.Series(data[:, 1]).value_counts()
    similarityScore = 0

    for i in data[:, 0]:
        if i not in colTwoUniqueCounts.keys():
            continue
        similarityScore += i * colTwoUniqueCounts[i]

    #print(f"The similarity score is {similarityScore:.0f}")
    return similarityScore
