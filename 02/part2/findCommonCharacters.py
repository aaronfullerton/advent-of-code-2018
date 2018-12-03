def findCommonCharacters():
    boxIds = open('./input.txt', 'r').read().splitlines()
    targetString1 = None
    targetString2 = None

    for boxId1 in boxIds:
        boxIds.remove(boxId1)
        for boxId2 in boxIds:
            if(isSimilar(boxId1, boxId2)):
                targetString1 = boxId1
                targetString2 = boxId2
                break

    differingCharacter = set(targetString1).difference(set(targetString2)).pop()
    targetList = list(targetString1)
    targetList.remove(differingCharacter)
    return "".join(targetList)


def isSimilar(boxId1, boxId2):
    count = 0
    characters1 = list(boxId1)
    characters2 = list(boxId2)

    for index, character in enumerate(characters1):
        if(character != characters2[index]):
            count += 1

        if(count > 1):
            return False

    return True


if __name__ == "__main__":
    print(findCommonCharacters())
