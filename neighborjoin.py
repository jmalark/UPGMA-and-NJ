import math
from readMatrix import *


def neighborjoin(distMat):

    distArr = []

    while len(distMat) > 3:

        bestPair = findBestPair(distMat, distArr)
        updateDistToNew(bestPair, distMat)



    return distArr

#avgDist in this refers to the average distance from the point to
#every other point except for itself and the it's partner point
#so it's almost the average distance

def findAvgDist(i, j, distMat):

    tempSumI = 0
    tempSumJ = 0

    for row in range(1, len(distMat)):
        if row != i and row != j:
            tempSumI += distMat[row][i]
            tempSumJ += distMat[row][j]


    avgDistI = tempSumI/(len(distMat) - 3)
    avgDistJ = tempSumJ/ (len(distMat) - 3)

    return (avgDistI, avgDistJ)


def findBestPair(distMat, distArr):

    bestPairVal = math.inf


    colMax = 1
    #for every pair of vertices
    for row in range(2, len(distMat)):
        for col in range(1, colMax + 1):

            avgDistTup = findAvgDist(row, col, distMat)

            tempBestPairVal = distMat[row][col] - avgDistTup[0] - avgDistTup[1]
            if tempBestPairVal < bestPairVal:
                bestPairVal = tempBestPairVal
                i = row
                j = col
                ui = avgDistTup[0]
                uj = avgDistTup[1]



        colMax += 1


    distIToIJ = .5*(distMat[i][j] + ui - uj)
    distJToIJ = .5*(distMat[i][j] + uj - ui)

    distArr.append([distMat[i][0], distIToIJ, distMat[0][j], distJToIJ])

    return (i, j)

def updateDistToNew(bestPair, distMat):

    i = bestPair[0]
    j = bestPair[1]
    Mij = distMat[i][j]

    #replace i's letter with ij's letter combination
    iLet = distMat[0][i]
    jLet = distMat[0][j]
    newLet = iLet + jLet

    distMat[i][0] = newLet
    distMat[0][i] = newLet

    #go across the row and down the column of i and update distances as though it is ij
    for cluster in range(1, len(distMat)):
        if cluster != i:
            Mik = distMat[i][cluster]
            Mjk = distMat[cluster][j]


            distToK = (Mik + Mjk - Mij)/2

            distMat[i][cluster] = distToK
            distMat[cluster][i] = distToK


    for cluster in range(len(distMat)):
        del distMat[cluster][j]


    del distMat[j]


