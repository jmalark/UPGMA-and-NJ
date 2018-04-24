from neighborjoin import *
from readMatrix import *
import argparse


def main():

    parser = argparse.ArgumentParser(description="Model a tree relationship of organisms based on a distance matrix")
    parser.add_argument("-i", help="Input file", required=True)
    parser.add_argument("-f", help= "Type of function: n for neighbor joining and u for UPGMA", required=True)

    args = parser.parse_args()

    inFile = args.i
    func = args.f
    func.lower()

    distMat = readMatrix(inFile)


    if func == "n":
        #run neighbor joining
        distArr = neighborjoin(distMat)
        strVer = distArrToVisualStyle(distArr)



    elif func == "u":
        #run upgma
        distArr = []

    else:
        print("Error: invalid commandline arguments")


main()