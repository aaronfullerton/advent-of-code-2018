def calculateChecksum():
    boxIds = open('./input.txt', 'r').read().splitlines()
    boxIdsWithTwoOfAnyLetter = filter(buildFilterFunction(2), boxIds)
    boxIdsWithThreeOfAnyLetter = filter(buildFilterFunction(3), boxIds)
    return len(boxIdsWithTwoOfAnyLetter) * len(boxIdsWithThreeOfAnyLetter)


def buildFilterFunction(numberOfLettersRequired):
    def filterFunction(boxId):
        tracker = {}
        characterList = list(boxId)

        # Count the number of characters in the boxId
        for character in characterList:
            if character in tracker:
                tracker[character] = tracker[character] + 1
            else:
                tracker[character] = 1

        # Check if any character appears the exact amount of times required
        for count in tracker.values():
            if(count == numberOfLettersRequired):
                return True

        return False

    return filterFunction


if __name__ == "__main__":
    print(calculateChecksum())
