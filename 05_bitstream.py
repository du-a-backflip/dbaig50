#<Dua> <Baig>
#<TNPG>
#SoftDev
#K<nn> -- <Bitstream/Bitstream/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
#<2024>-<09>-<17>
#time spent: <.7 hours>
import random
krewes = open("krewes.txt", "r")
info = krewes.read();
info = info.split("@@@")
info = info[:-1]

DictList = []

def makeDictList(InfoList):
    for i in InfoList:
        periodInfo = i.split("$$$")
        DictList.append (dict(period = periodInfo[0], devo = periodInfo[1], ducky = periodInfo[2]))


makeDictList(info)
print(DictList)
    
def ChooseDevo(ListDict):
    devo = ListDict[random.randint(0, len(ListDict)-1)]
    devo = devo["devo"]
    return devo;

print(ChooseDevo(DictList));