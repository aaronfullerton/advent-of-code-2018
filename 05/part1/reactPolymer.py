import arrow
import operator
import numpy
import re


def getPolymerString():
    return open('./input.txt', 'r').read()


def reactPolymer(polymer=getPolymerString()):
    polymerList = list(polymer)
    indicesToRemove = []
    skip = False

    for index, character in enumerate(polymerList):
        if(skip):
            skip = False
            continue
        else:
            characterNeeded = character.upper() if character.islower() else character.lower()

            if(len(polymerList) - 1 != index):
                if(polymerList[index + 1] == characterNeeded):
                    indicesToRemove.append(index)
                    indicesToRemove.append(index + 1)
                    skip = True

    if(indicesToRemove):
        for index in indicesToRemove:
            polymerList[index] = "$"
        polymer = reactPolymer("".join(polymerList).replace('$', ''))

    return polymer


if __name__ == "__main__":
    print(len(reactPolymer()))
