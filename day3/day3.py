# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:20:35 2024

@author: Julius
"""
# https://adventofcode.com/2024/day/3
import re


def mul(a, b):
    return a*b


storage = 0
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    sortedStrings = re.findall(r'mul\([0-9]+,[0-9]+\)', line)
    for element in sortedStrings:
        storage += eval(element)


storage2 = 0
state = True
for line in lines:
    newStrings = re.findall(r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", line)

    for element in newStrings:
        if element == "don't()" and state == True:
            state = False
        elif element == "do()" and state == False:
            state = True
        elif element == "do()" or element == "don't()":
            continue
        else:
            storage2 += eval(element) * state
