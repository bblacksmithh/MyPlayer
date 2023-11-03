import threading
import tkinter
import customtkinter
import pytube
from pytube import *

def startMP3Download():
    try: 
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        audio = ytObject.streams.get_audio_only()
        audio.download()
    except:
        print("YouTube link is invalid")
    print("Download Complete!")
    link.delete(0, 'end')

def startVideoDownload():
    try: 
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("YouTube link is invalid")
    print("Download Complete!")
    link.delete(0, 'end')

downloadAudioThread = threading.Thread(target=startMP3Download)
downloadVideoThread = threading.Thread(target=startVideoDownload)

#system settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#adding ui elements
title = customtkinter.CTkLabel(app, text="YouTube Downloader", corner_radius=20, fg_color="darkgrey",text_color="red")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#download button
downloadButtons = customtkinter.CTkFrame(app, width=600, height=50)
downloadButtons.pack(expand=True)
downloadMp3 = customtkinter.CTkButton(app, text="MP3", command=downloadAudioThread.start)
downloadVideo = customtkinter.CTkButton(app, text="Video", command=downloadVideoThread.start)
downloadMp3.pack(in_=downloadButtons ,padx=30, pady=30, )
downloadVideo.pack(in_=downloadButtons, padx=30, pady=30)

#run app
app.mainloop()