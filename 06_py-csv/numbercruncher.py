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
        CSV = csv.DictReader(file) #makes into dictionary
        for row in CSV:           
            infoList.append((row['Job Class'], row['Percentage'])) #adds rows of dictonary to a list
        return infoList[1:-1] #returns portion without titles and total


def chooseCareer(listFromFile):
    occupation = []
    percentage = []
    for i in listFromFile:
        occupation.append(i[0])
        percentage.append(float(i[1])/100) #makes separate list of percentages and occupations
    #print(percentage)
    return random.choices(occupation, percentage) #returns element in occupation based on weights in percentage list

print(chooseCareer(readCSV("occupations.csv")))
            