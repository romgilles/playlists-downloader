from sclib import SoundcloudAPI, Playlist
from helper import fileToTab,getRoot
import os

outputPath = getRoot()+"/output/soundcloud/"
dataPath = getRoot()+"/data/soundcloud/"

def downloadPlaylist(link):
    #connection à l'api 
    api = SoundcloudAPI()
    playlist = api.resolve(link)
    playlistName = playlist.title
    
    #../output/soundcloud/playlistName/
    playlistPath = outputPath+playlistName

    #on parse le fichier pour ajouter chaque titre déjà existant dans un tableau
    trackList = trackParser(playlistPath,playlistName)

    assert type(playlist) is Playlist

    #si le dossier n'existe pas on le crée
    if not os.path.exists(playlistPath):
                os.makedirs(playlistPath)
    #on parcourt chaque track de la playlist existante
    for track in playlist.tracks:
        exist = False
        fileName = f'./{track.artist} - {track.title}.mp3' 
        
        #on regarde dans la trackList existante si il existe déjà 
        for trackName in trackList:
            if trackName == fileName:
                print(fileName + " already downloaded")
                exist = True
                break
        #si le morceau n'existe pas
        if not exist:     
            print("downloading"+fileName)              
            #on créer le fichier si il n'existe pas
            
            try:
                with open(playlistPath+"/"+fileName, 'wb+') as file:
                    track.write_mp3_to(file)
                writeFile(playlistName,fileName)
            except:
                continue 
    return True 
            
#read a file with tracknames and convert it to a tab
def trackParser(playlistPath,playlistName):
    path = playlistPath+playlistName+".txt"
    tab= []
    #si house/house.txt n'existe pas
    if not os.path.exists(path):
        return tab
    else:
        tab = fileToTab(path)
        return tab
    
#write a new track name in the corresponding playlist
def writeFile(playlistName,trackName): 
    playlistFilePath = dataPath+playlistName+".txt"
    file = open(playlistFilePath,"a")
    file.write(trackName+"\n")
    file.close()
    return 

#check if a soundcloud playlist exist
def checkPlaylist(link):
    #connection à l'api 
    api = SoundcloudAPI()
    try:
        playlist = api.resolve(link)
        print(playlist.title+" OK")
        return True
    except:
        print("The link provided is not a playlist")
        return False

