import os
from pathlib import Path

def getRoot():
    abs = os.path.abspath(".")
    abs = Path(abs)
    rootPath = str(abs.parent.parent)
    return rootPath



def fileToTab(file):
    file = open(file,'r')
    tab = file.readlines()
    for i in range(len(tab)):
        tab[i] = tab[i].strip()
    return tab