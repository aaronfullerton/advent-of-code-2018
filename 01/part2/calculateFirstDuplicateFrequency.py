def calculateFirstDuplicateFrequency():
    input = open('./input.txt', 'r').read().splitlines()
    frequencyList = map(int, input)
    return recursivelyFindFirstDuplicateFrequency([], None, frequencyList)


def recursivelyFindFirstDuplicateFrequency(tracker, current, frequencyList):
    for value in frequencyList:

        if not current:
            current = value
            continue

        current = current + value

        if current in tracker:
            return current

        tracker.append(current)

    return recursivelyFindFirstDuplicateFrequency(tracker, current, frequencyList)


if __name__ == "__main__":
    print(calculateFirstDuplicateFrequency())
