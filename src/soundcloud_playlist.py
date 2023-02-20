from sclib import SoundcloudAPI, Track, Playlist
import os

def downloadPlaylist(link):
    #connection à l'api 
    api = SoundcloudAPI()
    playlist = api.resolve(link)
    playlistName = playlist.title
    path = "../output/"+playlistName
    #on parse le fichier pour ajouter chaque titre déjà existant dans un tableau
    trackList = trackParser(playlistName)
    assert type(playlist) is Playlist

    #si le dossier n'existe pas on le crée
    if not os.path.exists(path):
                os.makedirs(path)
    #on parcourt chaque track de la playlist existante
    for track in playlist.tracks:
        exist = False
        fileName = f'./{track.artist} - {track.title}.mp3' 
        
        #on regarde dans la trackList existante si il existe déjà 
        for trackName in trackList:
            if trackName == fileName+'\n':
                print(fileName + " already downloaded")
                exist = True
                break
        #si le morceau n'existe pas
        if not exist:     
            print("downloading"+fileName)              
            #on créer le fichier si il n'existe pas
            
            try:
                with open(path+"/"+fileName, 'wb+') as file:
                    track.write_mp3_to(file)
                writeFile(path,fileName)
            except:
                continue 
    return True 
            

def trackParser(playlistName):
    playlistFilePath = playlistName+"/"+playlistName+".txt" 
    path = "../output/"+playlistFilePath
    tab= []
    #si house/house.txt n'existe pas
    if not os.path.exists(path):
        return tab
    else:
        f = open(path,"r")
        tab = f.readlines()
        return tab

def writeFile(playlistName,trackName): 
    playlistFilePath = playlistName+"/"+playlistName+".txt"
    file = open(playlistFilePath,"a")
    file.write(trackName+"\n")
    file.close()
    return 

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
        
