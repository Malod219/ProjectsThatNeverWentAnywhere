from pygame import mixer
import os
import threading



mixer.init()
class player:
    def __init__(self):
        self.playing=False
        self.selected=[]
    def play(self):
        try:
            mixer.music.load("click.mp3")
            mixer.music.play(0)
        except:
            print("Filename not recognised")
        
    def pause(self):
        mixer.music.pause()
    def unpause(self):
        mixer.music.unpause()
    def queue(self,file):
        mixer.music.queue(file)

    def listMusic(self,folder):
        item_list = os.listdir(folder)
        print(item_list)
        file_list=[]
        for item in item_list:
            if os.path.isfile(folder+"/"+item):
                file_list.append(folder+"/"+item)
        self.selected=file_list
        print(file_list)
        print(self.selected)

    def playFilesInFolder(self):
        mixer.music.load("click.mp3")
        mixer.music.play(2)
        for file in self.selected:
            mixer.music.queue(file)

p=player()
while True:
    try:
        choice=int(input("1-Play\n2-Pause\n3-Unpause\n4-Queue\n5-Select+List files in folder\n6-Queue selected files"))
    except:
        pass
    if choice==1:
        p.play()
    elif choice==2:
        p.pause()
    elif choice==3:
        p.unpause()
    elif choice==4:
        fileName=str(input("Enter the filename"))
        p.queue(fileName)
    elif choice==5:
        folder=str(input("Enter the folder"))
        p.listMusic(folder)
    elif choice==6:
        p.playFilesInFolder()
