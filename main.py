import multiprocessing
import threading
import time
from soundcloud_playlist import downloadPlaylist
import argparse

def removeEnd(string):
    return string.strip()

#todo fix lines
def fileToTab(file):
    file = open(file,'r')
    tab = file.readlines()
    for i in range(len(tab)):
        tab[i] = tab[i].strip()
    return tab

# Fonction pour le thread d'ajout de lien
def link_adder():
    print("Please enter a command")
    link = input('>>')
    command = link.split(" ")
    if command[0] == "add":
        file = open("playlists.txt","w")
        file.write(command[1])
        file.close()
    return



# Démarrer le thread d'ajout de lien
#init
linkList = fileToTab("playlists.txt")
status = False 
print(linkList)

def downloadCheck():
    while status:
        print("\n")
        for link in linkList:
            downloadPlaylist(link)
        time.sleep(300)
    return

        
while True:
    link = input('>>')
    command = link.split(" ")
    if command[0] == "add":
        file = open("playlists.txt","a")
        file.write(command[1]+'\n')
        file.close()
    elif command[0] == "run":
        if status == True:
            print("The program is already running")
        else:
            status = True
            t = threading.Thread(target=downloadCheck,daemon=True)
            t.start()
            
            print("Program started")
            
            
        
    elif command[0] == "isRunning":
        if status:
            print("yes")
        else:
            print("no")

    elif command[0] == "stop":
        if status == True:
            status = False
            print("Not running anymore")
            
        else:
            print("The program is not running")
    
    elif command[0] == "exit":
        break


    