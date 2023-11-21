import random
from tkinter import PhotoImage
import re
import datetime as date
from datetime import datetime
import LanguageDictionary as Lg
import DataBaseLocal as DBL
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
picture = "../assets/flags/Avatar-Profile.png"
picpassword = "NONE"
Songs1 = ["","",""]
Palette = "WHITE"
Texture = "METAL"

def selecPalett(Color):
    global Palette
    if isinstance(Color, str):
        Palette = Color
        print(Color)
    else:
        return 0



def selectTexture(TEXTURE):
    global Texture
    if isinstance(Texture, str):
        Texture = TEXTURE
        return 1
    else:
        return 0



def validar_tarjeta(numero, fecha_vencimiento, cvc, nombre_titular):
    # Validar el número de tarjeta (16 dígitos)
    if not re.match(r'^\d{16}$', numero):
        return False, Lg.Dt["Numero de tarjeta invalido"][Lg.language]

    # Validar la fecha de vencimiento (formato MM/YY)
    try:
        fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%m/%y')
        if fecha_vencimiento < datetime.now():
            return False, Lg.Dt["Tarjeta vencida"][Lg.language]
    except ValueError:
        return False, Lg.Dt["Formato de fecha incorrecto"][Lg.language]

    # Validar el código de seguridad (3 o 4 dígitos)
    if not re.match(r'^\d{3,4}$', cvc):
        return False, Lg.Dt["Codigo de seguridad invalido"][Lg.language]

    # Validar el nombre del titular (solo caracteres alfabéticos y espacios)
    if not re.match(r'^[a-zA-Z\s]+$', nombre_titular):
        return False, Lg.Dt["Nombre del titular invalido"][Lg.language]
    return True, Lg.Dt["Tarjeta Valida"][Lg.language]

"""def UsernameCheck(Username):
    global username
    if isinstance(username,str):
        if 8<= len(Username) <16:
            username = Username
            return 1
        else:
            return 0
    else:
        return 0"""


def LastNameCheck(last_name):

    if isinstance(last_name, str):
        if 2 <= len(last_name) <= 30:
            return last_name # Apellido válido
        else:
            return 0  # Longitud del apellido no válida
    else:
        return 0  # Tipo de dato no válido

def FirstNameCheck(first_name):
    if isinstance(first_name, str):
        if 2 <= len(first_name) <= 20:
            return first_name # Nombre válido
        else:
            return 0  # Longitud del nombre no válida
    else:
        return 0  # Tipo de dato no válido

def MailCheck(Mail):

    if isinstance(Mail, str):
        #if DBL.is_email_registered(Mail):
            if re.search(r'@', Mail):
                MailSplit = Mail.split("@")
                if MailSplit[1] == "gmail.com" or MailSplit[1] == "hotmail.com" or MailSplit[1]=="outlook.com" or MailSplit[1]=="yahoo.com" or MailSplit[1]=="icloud.com" or MailSplit[1]=="live.com" or MailSplit[1]=="estudiantec.cr" or MailSplit[1]=="hotmail.es":
                    return Mail

                else:
                    return 0, Lg.Dt["Dominio no valido"][Lg.language]
            else:
                return 0, Lg.Dt["Falta @ en el correo"][Lg.language]
        #else:
           # return 0, "Correo ya registrado"
    else:
        return 0 , Lg.Dt["Correo no valido"][Lg.language]

"""def PasswordCheck(Password):
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
                        return  "Falta caracter especial"
                else:
                    return "Falta dígito"
            else:
                return "Falta letra mayúscula"
        else:
            return "Longitud de contraseña no válida"
    else:
        return 0  # Tipo de dato no válido"""
    

def SelectDate(datese):

    if isinstance(datese, str):
        date_part = datese.split("/")
        month = int(date_part[0])
        day = int(date_part[1])
        if 0 <= int(date_part[2]) <= 23:
            year = int("20"+date_part[2])
        elif 30<= int(date_part[2]) <= 99:
            year = int("19" + date_part[2])
        dateborn = date.datetime(year, month, day)
        Age = date.datetime.today().year-dateborn.year
        return Age
    else:
        return 0


def validar_usuario(username):
    """
    Valida que el nombre de usuario no contenga obscenidades.
    """
    palabras_prohibidas = ["Caca", "Shit", "Sexo, Sex,Bullshit, Malparido,SEX,sex,SEXO,sexo"]  # Añade las palabras que desees prohibir
    if not isinstance(username, str):
        return False

    if DBL.is_username_registered(username):
        return False, Lg.Dt["Usuario en uso"][Lg.language]

    if len(username) < 8 or len(username) > 16:
        return False, Lg.Dt["El usuario debe ser mayor 8 caracteres y menor que 16"][Lg.language]
    for palabra in palabras_prohibidas:
        if palabra.lower() in username.lower():
            return False, Lg.Dt["Palabra inapropiada: "][Lg.language]+ palabra.lower()
    return True, ""



def verificar_contrasenas(password, password_check):
    if password == password_check:
         return password_check
    else:
        return 0

def validar_contrasena(password):
        """
        Valida que la contraseña cumpla con los siguientes requisitos:
        - Mínimo 8 caracteres
        - Máximo 16 caracteres
        - Al menos una letra mayúscula
        - Al menos una letra minúscula
        - Al menos un número
        - Al menos un carácter especial
        """
        if (8 <= len(password) <= 16 and
                re.search("[a-z]", password) and
                re.search("[A-Z]", password) and
                re.search("[0-9]", password) and
                re.search("[@#$%^&+=.,!/*()-<>]", password)):
            return True
        return False


print(validar_tarjeta("1478963214789632","12/24","121","Samuel Xd"))