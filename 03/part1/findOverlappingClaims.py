import numpy


def convertRawClaim(claim):
    # Example claim: #1 @ 265,241: 16x26
    claimDict = {}
    data = claim.split(" ")
    claimCoordinates = data[2][:-1].split(",")
    claimDimensions = data[3].split("x")

    claimDict["id"] = int(data[0][1:])
    claimDict["x"] = int(claimCoordinates[0])
    claimDict["y"] = int(claimCoordinates[1])

    claimDict["width"] = int(claimDimensions[0])
    claimDict["height"] = int(claimDimensions[1])

    return claimDict


def getClaims():
    rawClaims = open('./input.txt', 'r').read().splitlines()
    return map(convertRawClaim, rawClaims)


def placeClaimsInMatrix(claims):
    matrix = numpy.zeros(shape=(1000, 1000))
    for claim in claims:
        xRange = numpy.arange(claim['x'], claim['x'] + claim['width'])
        yRange = numpy.arange(claim['y'], claim['y'] + claim['height'])

        for x in xRange:
            for y in yRange:
                matrix[x][y] = matrix[x][y] + 1

    return matrix


def findOverlappingClaims():
    claims = getClaims()
    matrix = placeClaimsInMatrix(claims)
    counter = 0

    for row in matrix:
        for cell in row:
            if(cell > 1):
                counter = counter + 1

    return counter


if __name__ == "__main__":
    print(findOverlappingClaims())
