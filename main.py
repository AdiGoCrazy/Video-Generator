from customtkinter import *
from captionedvideo import *
import dictionaries

set_appearance_mode("Dark")

#Image + Background Video + Reaction Clip are combined to make a artificial attention grabbing video.
def img_reaction():
    #Creates a UI for customization of the videos to be generated 
    window = CTk()
    window.title("img_reaction")
    window.configure(background="grey")
    window.geometry("400x400")
    window.resizable = False  
    
    #Label
    title = CTkLabel(window,text = "Image Reaction",font=("Calibri",40),bg_color="#385E94",width=300,height=80,corner_radius=10)
    title.place(x=50,y=0)
    channel = CTkLabel(window,text="Channel Details",font=("Calibri",20),width=300,height=10,bg_color="#385E94")
    channel.place(x=50,y=100)
    video_details = CTkLabel(window,text="Video Details",font=("Calibri",20),width=300,height=10,bg_color="#385E94")
    video_details.place(x=50,y=160)
    
    #Entry
    channel_name = CTkEntry(window,width=100,height=20)
    channel_name.place()
    username_entry = CTkEntry(window,width=200,height=20)
    username_entry.place(x=50,y=130)
    number_entry = CTkEntry(window,width=50,height=20)
    number_entry.place(x=260,y=130)
    x=10
    #ComboBox
    reactor_combobox = CTkComboBox(window,values=list(dictionaries.reactors.keys()),width=100,height=20)
    reactor_combobox.place(x=50,y=190)
    background_video = CTkComboBox(window,values=list(dictionaries.background_videos.keys()),width=100,height=20)
    background_video.place(x=50,y=220)
    music = CTkComboBox(window,values=["None","Other"],width=100,height=20)
    music.place(x=170,y=190)
    
    #Button
    generate = CTkButton(window,text="Generate",font=("Calibri",30),width=200,height=90,command=lambda:videogenerate([reactor_combobox.get(),background_video.get(),music.get()],[str(username_entry.get()),number_entry.get()]))
    generate.place(x=100,y=250)
    
    window.mainloop()
    
#Main Window where you can select what kind of artificial video to generate 
window = CTk()
window.title("Video Generator")
window.configure(background="grey")
window.geometry("400x400")
window.resizable = False


#Panel
panel = CTkFrame(window,width=300,height=200,corner_radius=10,border_color="black",border_width=5)
panel.place(x=50,y=100)


#Labels
title = CTkLabel(window,text = "Video Generator",font=("Calibri",40),bg_color="#385E94",width=300,height=80,corner_radius=10)
title.place(x=50,y=0)


#Buttons
videopost_button = CTkButton(window,text="Ocean\nVideo Funny",width=100,height=85,command=lambda:img_reaction(),anchor="center",corner_radius=10,border_color="black",border_width=5)
videopost_button.place(x=160,y=110)



window.mainloop()



    
    

        


    