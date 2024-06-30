#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def openChatWindow():

   
    print("\n\t\t\t\tMusic Messenger")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.config(bg='LightSkyBlue')

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    selectlabel = Label(window, text= "Select Song", font = ("Calibri",8))
    selectlabel.place(x=2, y=1)

    name = Entry(window,width =30,font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    connectserver = Button(window,text="Connect to Chat Server",bd=1, font = ("Calibri",10))
    connectserver.place(x=350,y=6)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text= "Active Users", font = ("Calibri",10))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', font = ("Calibri",10), borderwidth=2, bg='LightSkyBlue')
    listbox.place(x=10, y=30)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play",bd=1, width=10, bg="SkyBlue", font = ("Calibri",10))
    playButton.place(x=30,y=200)

    stopButton=Button(window,text="Stop",bd=1,width=10, bg="SkyBlue", font = ("Calibri",10))
    stopButton.place(x=200,y=200)

    Upload=Button(window,text="Upload", width=10,bd=1,bg="skyBlue", font = ("Calibri",10))
    Upload.place(x=30,y=250)

    infoLabel = Label(window, text = "", fg="blue", font = ( "Calibri", 8))
    infoLabel.place(x=4, y=280)

    Download = Button(window, text= "Download", width=10,bd=1,bg='Skyblue', font = ("Calibri", 10))
    Download.place(x=200,y=250)

    scrollbar2 = Scrollbar(textarea)
    scrollbar2.place(relheight = 1, relx = 1)
    scrollbar2.config(command = listbox.yview)

    attach=Button(window,text="Attach & Send", bd=1, font = ("Calibri",10))
    attach.place(x=10,y=305)

    text_message = Entry(window, width =43, font = ("Calibri",12))
    text_message.pack()
    text_message.place(x=98,y=306)

    send=Button(window,text="Send",bd=1, font = ("Calibri",10))
    send.place(x=450,y=305)

    filePathLabel = Label(window, text= "",fg= "blue", font = ("Calibri", 8))
    filePathLabel.place(x=10, y=330)
  
    
  
  
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    openChatWindow()

setup()
