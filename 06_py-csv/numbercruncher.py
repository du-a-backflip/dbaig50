#<Dua> <Baig>
#<TNPG>
#SoftDev
#K<nn> -- <Divine your Destiny/Reading CSV files/Reads a CSV File and returns result based on percentage data within...>
#<2024>-<09>-<19>
#time spent: <~1.5 hours>

import csv
import random

def readCSV(filename):
    infoList = []
    with open (filename, mode = 'r') as file:
        CSV = csv.reader(file)
        for i in CSV:
            infoList.append(i)
        return infoList[1:-1]


def chooseCareer(listFromFile):
    occupation = []
    percentage = []
    for i in listFromFile:
        occupation.append(i[0])
        percentage.append(float(i[1])/100)
    #print(percentage)
    return random.choices(occupation, percentage)

print(chooseCareer(readCSV("occupations.csv")))
            