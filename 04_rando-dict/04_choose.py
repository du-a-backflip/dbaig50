#<Dua> <Baig>
#<TNPG>
#SoftDev
#K<nn> -- <Choose Random Devo/Python Lists and Dictionaries/Chooses a random devo from krewes dictionary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
#<2024>-<09>-<16>
#time spent: <0.8 hours>
import random

krewes = {
           4: [ 
            'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
            'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
            'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
            'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
            ],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }

def ChooseDevo():
    period = list(krewes.keys())
    period = period[random.randint(0, len(period)-1)]
    devo = list(krewes[period]);
    devo = devo[random.randint(0, len(devo)-1)]
    return devo;