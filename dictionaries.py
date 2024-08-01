#This is where data of the current options available for customization of videos are generated(captionedVideo)

import os

music_list={}
background_videos={}
reactors={}
for i in os.listdir("captionedvideo/"+"BackgroundVideos"):
    background_videos[i[0:-4]] = i 
for i in os.listdir("captionedvideo/"+"Music"):
    music_list[i[0:-4]] = i
for i in os.listdir("captionedvideo/"+"Reactor"):
    reactors[i[0:-4]] = i

if __name__ == "__main__":
    pass

