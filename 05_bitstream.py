#<Frist> <Lsat>
#<TNPG>
#SoftDev
#K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
#<yyyy>-<mm>-<dd>
#time spent: <elapsed time in hours, rounded to nearest tenth>
#<TNPG>
#SoftDev
#K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
#<yyyy>-<mm>-<dd>
#time spent: <elapsed time in hours, rounded to nearest tenth>

krewes = open("krewes.txt", "r")
info = krewes.read();
info = info.split("@@@")

krewesDict = {}
period = []
for i in info:
    period = i.split("$$$")
    print(period)
    
