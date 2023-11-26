import threading
import tkinter
import customtkinter
import pytube
from pytube import *
from tkinter import messagebox

def downloadCompleteMessage():
    downloadComplete = messagebox.showinfo("Download", "Download Complete!")

def startMP3Download():
    try: 
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        audio = ytObject.streams.get_audio_only()
        audio.download()
    except:
        print("YouTube link is invalid")
    print("Download Complete!")
    downloadCompleteMessage()
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
    downloadCompleteMessage()
    link.delete(0, 'end')

#system settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("MyPlayer")

#adding ui elements
title = customtkinter.CTkLabel(app, text="MyPlayer", corner_radius=20, fg_color="darkgrey",text_color="#8F0B0B")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#download button
downloadButtons = customtkinter.CTkFrame(app, width=600, height=50)
downloadButtons.pack(expand=True)

#download buttons initialized
#multithreading implemented with download functions to prevent application from freezing
downloadMp3 = customtkinter.CTkButton(app, text="MP3", command=threading.Thread(target=startMP3Download).start)
downloadVideo = customtkinter.CTkButton(app, text="Video", command=threading.Thread(target=startVideoDownload).start)

#buttons packed in GUI
downloadMp3.pack(in_=downloadButtons ,padx=30, pady=30, )
downloadVideo.pack(in_=downloadButtons, padx=30, pady=30)

#run app
app.mainloop()