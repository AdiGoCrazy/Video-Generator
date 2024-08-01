#This is the library where video generation is done by moviepy by giving it input and details 
#for the video to be generated()

import dictionaries
from moviepy.editor import *


def videogenerate(videodetails,accountsdetails):
        def execute(username,number,password):
            import instaloader
            L = instaloader.Instaloader()
            L.login(username,password)
            profile = instaloader.Profile.from_username(L.context,username)
            i=0
            for post in profile.get_posts():
                if post.typename == "GraphImage":
                    L.download_post(post,target=profile.username)
                    i += 1
                    if i >= int(number):
                        break
            print("Done")
        
        def movefiles(username):
            import shutil
            for i in os.listdir(username):
                if i.endswith(".jpg"):
                    shutil.move(username+"/"+i,"captionedVideo/Photos/"+i)
        
        from moviepy.video.fx.resize import resize
        import os
        
        execute(accountsdetails[0],accountsdetails[1])
        movefiles(accountsdetails[0])
        t = "captionedvideo/"
        background_video = VideoFileClip(t+"BackgroundVideos/"+dictionaries.background_videos[videodetails[1]],target_resolution=(1920,1080)).without_audio()
        dur = background_video.duration
        background_video = background_video.set_duration(dur/2)
    
        react = VideoFileClip(t+"Reactor/"+dictionaries.reactors[videodetails[0]],target_resolution=(1800,1300)).set_position(("center","bottom")).set_duration(dur/2)
        react = react.fx(vfx.mask_color,color=[0,255,8],thr=150,s=6)
        o = 0
        for i in os.listdir(t+"Photos"):
            if i.endswith("jpg"):
                o += 1
                image = ImageClip(t+"Photos/"+i,duration=dur/2)
                image = resize(image,width=1100,height=1000)
                image = image.set_position((20,50))
                final_clip = CompositeVideoClip([background_video,image,react])
                final_clip.write_videofile(str(o) + ".mp4",codec = "png")


if __name__ == "__main__":
    pass