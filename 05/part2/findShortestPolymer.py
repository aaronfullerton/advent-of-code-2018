def getPolymerString():
    return open('./input.txt', 'r').read()


def getPolarOpposite(character):
    return character.upper() if character.islower() else character.lower()


def reactPolymer(polymer=getPolymerString()):
    polymerList = list(polymer)
    indicesToRemove = []
    skip = False

    for index, character in enumerate(polymerList):
        if(skip):
            skip = False
            continue
        else:
            characterNeeded = getPolarOpposite(character)

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


def testPolymers():
    polymer = getPolymerString()
    shortestLength = None
    polymerSet = set(getPolymerString())

    for character in polymerSet:
        testPolymer = str(polymer)
        testPolymer = testPolymer.replace(character, '')
        testPolymer = testPolymer.replace(getPolarOpposite(character), '')
        length = len(reactPolymer(testPolymer))

        if(not shortestLength or length < shortestLength):
            shortestLength = length

    return shortestLength


if __name__ == "__main__":
    print(testPolymers())
