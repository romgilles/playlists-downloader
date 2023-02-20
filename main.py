import threading
from soundcloud_playlist import downloadPlaylist,checkPlaylist


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

def downloadCheck():
    for link in linkList:
        downloadPlaylist(link)
    return
print("*****Welcome to Soundcloud Downloader*****")
print("Enter help to show commands")

while True:
    link = input('>>')
    command = link.split(" ")
    
    if command[0] == "add" and command[1] != None:
        print("checking playlist...")
        if(checkPlaylist(command[1])):
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

    elif command[0] == "list":
        for playlist in linkList:
            print(playlist)
    
    elif command[0] == "help":
        print("run - Start checking all playlists for updates and download new songs")
        print("add link - Add a new playlist to download")
        print("list - list all Playlists")
        print("exit - Exit the program")



    
    elif command[0] == "exit":
        break


    