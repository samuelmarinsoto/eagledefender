from collections import namedtuple


language = 2
def changeLanguage(lang):
    global language
    if isinstance(lang, str):
    
        if lang == "English":   
            language = 0
        elif lang == "Español":
            language = 1
        elif lang == "Français":
            language = 2
    else:
        return 0 

# Define un namedtuple para las traducciones
Translation = namedtuple("Translation", ["en", "es", "fr"])

# Define el diccionario con las traducciones
dic = {
    "Game": Translation(en="Game", es="Juego", fr="Jeu"),
    "Login": Translation(en="Login", es="Inicio de sesion", fr="Se connecter"),
    "Register": Translation(en="Register", es="Registro", fr="S'inscrire"),
    "Back": Translation(en="Back", es="Atras", fr="Retour"),
    
}

#EXAMPLE Lg.dic["Login"][Lg.language]