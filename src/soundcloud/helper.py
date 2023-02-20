#todo fix lines
def fileToTab(file):
    file = open(file,'r')
    tab = file.readlines()
    for i in range(len(tab)):
        tab[i] = tab[i].strip()
    return tab