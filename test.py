
from readMatrix import *
from neighborjoin import *

def main():

    distMat = readMatrix("abcde.txt")


    for row in distMat:
        print(row)


    print("\n\n\n")



    distArr = neighborjoin(distMat)


    for row in distMat:
        print(row)


    print("\n\n\n")

main()