import threading
from soundcloud_playlist import downloadPlaylist,checkPlaylist
from helper import fileToTab

def downloadCheck():
    for link in linkList:
        downloadPlaylist(link)
    return

#Démarrer le thread d'ajout de lien
#init
linkList = fileToTab("../playlists.txt")

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
        print("Program started")
        downloadCheck()
        

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


    