# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:48:30 2024

@author: Julius
"""
# https://adventofcode.com/2024

import numpy as np

with open("input.txt", "r") as file:
    lines = file.read().splitlines()


array = np.array([list(line) for line in lines])


def wordFinder(array, word):
    length = len(array)
    hcounter, vcounter, dcounter, d2counter = 0, 0, 0, 0
    for i in range(length):
        for j in range(length):
            horizontalWord, verticalWord, diagonalWord, diagonal2Word = 0, 0, 0, 0
            if j < length-3:
                horizontalWord = array[i, j] + array[i,
                                                     j+1] + array[i, j+2] + array[i, j+3]

            if i < length-3:
                verticalWord = array[i, j] + array[i+1, j] + \
                    array[i+2, j] + array[i+3, j]
            if i < length-3 and j < length - 3:
                diagonalWord = array[i, j] + array[i+1, j+1] + \
                    array[i+2, j+2] + array[i+3, j+3]
            if i < length-3 and j > 2:
                diagonal2Word = array[i+3, j-3] + array[i +
                                                        2, j-2] + array[i+1, j-1] + array[i, j]
            if horizontalWord == "XMAS":
                hcounter += 1
            if horizontalWord == "SAMX":
                hcounter += 1
            if verticalWord == "XMAS":
                vcounter += 1
            if verticalWord == "SAMX":
                vcounter += 1
            if diagonalWord == "XMAS":
                dcounter += 1
            if diagonalWord == "SAMX":
                dcounter += 1
            if diagonal2Word == "XMAS":
                d2counter += 1
            if diagonal2Word == "SAMX":
                d2counter += 1
    return hcounter, vcounter, dcounter, d2counter


def xmasFinder(array):
    length = len(array)
    masCounter = 0
    for i in range(length):
        for j in range(length):
            diagonalWord, diagonal2Word = 0, 0
            if i < length-1 and i > 0 and j < length-1 and j > 0:
                diagonalWord = array[i-1, j-1] + array[i, j] + array[i+1, j+1]
            if i < length-1 and i > 0 and j > 0 and j < length-1:
                diagonal2Word = array[i+1, j-1] + array[i, j] + array[i-1, j+1]
            if (diagonalWord == "MAS" or diagonalWord == "SAM") and (diagonal2Word == "MAS" or diagonal2Word == "SAM"):
                masCounter += 1
    return masCounter


count = wordFinder(array, "xmas")
masCount = xmasFinder(array)
print(f"occurences of xmas: {sum(count)}")
print(f"occurences of mas in x-shape: {masCount}")
