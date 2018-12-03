def calculateFrequency():
    input = open('./input.txt', 'r').read().splitlines()
    frequencyList = map(int, input)
    return sum(frequencyList)


if __name__ == "__main__":
    print(calculateFrequency())
