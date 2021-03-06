import arrow
import operator
import numpy
import re


def convertGuardData(row):
    row = row.split("]")
    timestamp = arrow.get(row[0][1:]).timestamp
    event = row[1][1:]
    return (timestamp, event)


def getSortedGuardData():
    rawData = open('./input.txt', 'r').read().splitlines()
    guardData = map(convertGuardData, rawData)
    return sorted(
        guardData,
        key=operator.itemgetter(0)
    )


def organizeData():
    tracker = {}
    sortedData = getSortedGuardData()
    currentGuard = None
    sleepStarts = None
    sleepEnds = None
    for tup in sortedData:
        time = arrow.get(tup[0])
        event = tup[1]

        if("#" in event):
            currentGuard = int(re.search(r'\d+', event).group())
        if("falls" in event):
            sleepStarts = time
        if("wakes" in event):
            sleepEnds = time

            startMinute = sleepStarts.format("mm")
            endMinute = sleepEnds.format("mm")
            asleepMinutes = numpy.arange(int(startMinute), int(endMinute))

            for minute in asleepMinutes:
                if(minute in tracker and tracker[minute] is not None):
                    currentList = tracker[minute]
                    currentList.append(currentGuard)
                    tracker[minute] = currentList
                else:
                    tracker[minute] = [currentGuard]

            sleepStarts = None
            sleepEnds = None

    return tracker


def analyzeData():
    tracker = organizeData()
    highestCount = 0
    mostConsistenGuard = None
    mostConsistentMinute = None
    for minute, guards in tracker.items():
        for guard in guards:
            currentCount = guards.count(guard)
            if currentCount > highestCount:
                highestCount = currentCount
                mostConsistenGuard = guard
                mostConsistentMinute = minute

    return (mostConsistenGuard, mostConsistentMinute)


if __name__ == "__main__":
    tup = analyzeData()
    print("Most Consistent Guard", tup[0])
    print("Most Consistent Minute", tup[1])
    print("Product", tup[0] * tup[1])
