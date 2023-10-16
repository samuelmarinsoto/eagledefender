import random
from tkinter import PhotoImage
"""

In this .py the user information will be saved or collected of server

"""

LOGGED = False
Member = False
PLAY = False
name =  "NONE"
lastmame = "NONE"
age = "NONE"
password = "NONE"
username = "NONE"
picture = "assets/flags/Avatar-Profile.png"
picpassword = "NONE"

def LoggedComprobation():
    global LOGGED,Member, PLAY, name, password, username, picture, picpassword
    if LOGGED and Member:
        PLAY = True
        name = "ass"
        #password =
        #username =
        #picture =
        #picpassword =

    elif LOGGED:
        PLAY = True
        name = "Guest" + str(random.randint(1000,1500))
        password = "NONE"
        username = "NONE"
        picture = "NONE"
        picpassword = "NONE"

    else:
        PLAY = False
    return 0

"""def changePic(PATH):
    global picture
    picture = PATH"""
