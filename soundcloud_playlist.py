from sclib import SoundcloudAPI, Track, Playlist
import os

def downloadPlaylist(link):
    #connection à l'api 
    api = SoundcloudAPI()
    try:
        playlist = api.resolve(link)
    except:
        return False
    
    playlistName = playlist.title
    
    #on parse le fichier pour ajouter chaque titre déjà existant dans un tableau
    trackList = trackParser(playlistName)
    
    assert type(playlist) is Playlist

    #si le dossier n'existe pas on le crée
    if not os.path.exists(playlistName):
                os.makedirs(playlistName)
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
                with open(playlistName+"/"+fileName, 'wb+') as file:
                    track.write_mp3_to(file)
                writeFile(playlistName,fileName)
            except:
                continue 
    return True 
            

def trackParser(playlistName):
    playlistFilePath = playlistName+"/"+playlistName+".txt" 
    tab= []
    #si house/house.txt n'existe pas
    if not os.path.exists(playlistName):
        return tab
    else:
        f = open(playlistFilePath,"r")
        tab = f.readlines()

        return tab


def writeFile(playlistName,trackName): 
    playlistFilePath = playlistName+"/"+playlistName+".txt"
    file = open(playlistFilePath,"a")
    file.write(trackName+"\n")
    file.close()
    return 

    
