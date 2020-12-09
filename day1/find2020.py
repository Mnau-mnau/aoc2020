import sys
import os
import re
import glob

def loadData():
    pathToFile = 'day1/input.txt'
    with open(pathToFile) as fp:
        string = fp.read()
    return string

data = loadData().split('\n')

def is2020(first, second):
    if first + second == 2020:
        return True
    return False

for num in data:
    multiply = None
    for num2 in data:
        if (int(num) + int(num2)) == 2020:
            print(num, num2)
            multiply = int(num) * int(num2)
            break
        else:
            pass
    if multiply:
        print('multiply', multiply)
        break
    else:
        pass

for num in data:
    multiply = None
    for num2 in data:
        for num3 in data:
            if (int(num) + int(num2) + int(num3)) == 2020:
                print(num, num2, num3)
                multiply = int(num) * int(num2) * int(num3)
                break
            else:
                pass
        if multiply:
            print('multiply', multiply)
            break
        else: pass
    if multiply:
        print('multiply', multiply)
        break
    else:
        pass