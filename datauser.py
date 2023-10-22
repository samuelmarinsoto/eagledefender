import random
from tkinter import PhotoImage
import re
"""

In this .py the user information will be saved or collected of server

"""

LOGGED = False
Member = False
PLAY = False
name =  "NONE"
lastname = "NONE"
age = "NONE"
mail = "NONE"
password = "NONE"
username = "NONE"
picture = "assets/flags/Avatar-Profile.png"
picpassword = "NONE"
Songs1 = ["","",""]
Palette = "WHITE"


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

def selecPalett(Color):
    global Palette
    if isinstance(Color, str):
        Palette = Color
        print(Color)
    else:
        return 0
    
def UsernameCheck(Username):
    global username
    if isinstance(username,str):
        if 8<= len(Username) <16:
            username = Username
            return 1
        else:
            return 0
    else:
        return -1


def LastNameCheck(last_name):
    global lastname
    if isinstance(last_name, str):
        if 2 <= len(last_name) <= 30:
            lastname = last_name
            return 1  # Apellido válido
        else:
            return 0  # Longitud del apellido no válida
    else:
        return -1  # Tipo de dato no válido

def FirstNameCheck(first_name):
    global name
    if isinstance(first_name, str):
        if 2 <= len(first_name) <= 20:
            name = first_name
            return 1  # Nombre válido
        else:
            return 0  # Longitud del nombre no válida
    else:
        return -1  # Tipo de dato no válido

def MailCheck(Mail):
    global mail
    
    if isinstance(Mail, str):
        if re.search(r'@', Mail):
            MailSplit = Mail.split("@")
            if MailSplit[1] == "gmail.com" or MailSplit[1] == "hotmail.com" or MailSplit[1]=="outlook.com" or MailSplit[1]=="yahoo.com" or MailSplit[1]=="icloud.com" or MailSplit[1]=="live.com":
                mail = Mail
                return 1
            else:
                return 0
        else:
            return -1
    else:
        return -1  # Tipo de dato no válido

def PasswordCheck(Password):
    global password
    if isinstance(Password, str):
        # Verifica la longitud de la contraseña
        if 8 <= len(Password) <= 15:
            # Verifica si la contraseña contiene al menos una letra mayúscula
            if re.search(r'[A-Z]', Password):
                # Verifica si la contraseña contiene al menos un dígito
                if re.search(r'\d', Password):
                    # Verifica si la contraseña contiene al menos un caracter especial (por ejemplo, !@#$%^&)
                    if re.search(r'[!@#$%^&.]', Password):
                        password = Password
                        return 1  # Contraseña válida
                    else:
                        return 0  # Falta caracter especial
                else:
                    return 0  # Falta dígito
            else:
                return 0  # Falta letra mayúscula
        else:
            return 0  # Longitud de contraseña no válida
    else:
        return -1  # Tipo de dato no válido

