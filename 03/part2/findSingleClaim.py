import numpy


def convertRawClaim(claim):
    # Example claim: #1 @ 265,241: 16x26
    claimDict = {}
    data = claim.split(" ")
    claimCoordinates = data[2][:-1].split(",")
    claimDimensions = data[3].split("x")

    claimDict["id"] = data[0]
    claimDict["x"] = int(claimCoordinates[0])
    claimDict["y"] = int(claimCoordinates[1])

    claimDict["width"] = int(claimDimensions[0])
    claimDict["height"] = int(claimDimensions[1])

    return claimDict


def getClaims():
    rawClaims = open('./input.txt', 'r').read().splitlines()
    return map(convertRawClaim, rawClaims)


def placeClaimsInMatrix(claims):
    matrix = numpy.zeros(shape=(1000, 1000), dtype=int)
    matrix = matrix.astype(str)

    for claim in claims:
        xRange = numpy.arange(claim['x'], claim['x'] + claim['width'])
        yRange = numpy.arange(claim['y'], claim['y'] + claim['height'])
        for x in xRange:
            for y in yRange:
                if (matrix[x][y] == "0"):
                    matrix[x][y] = claim['id']
                else:
                    matrix[x][y] = matrix[x][y] + "," + claim['id']

    return matrix


def findSingleClaim():
    claims = getClaims()
    matrix = placeClaimsInMatrix(claims)
    tracker = {}

    for row in matrix:
        for cell in row:
            if(cell != '0' and "," in cell):
                claimsInCell = cell.split(",")
                for claimId in claimsInCell:
                    tracker[claimId] = True
            elif(cell != '0' and cell not in tracker):
                tracker[cell] = False

    for claimId, value in tracker.items():
        if(value == False):
            return claimId


if __name__ == "__main__":
    print(findSingleClaim())
