from collections import namedtuple


language = 1
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
    "Member": Translation(en="Member", es="Miembro", fr="Membre"),
    "Pay section": Translation(en="Pay section", es="Seccion de pago", fr="Section de paiement"),
    "Pay": Translation(en="Pay", es="Pagar", fr="Payer"),
    "Back": Translation(en="Back", es="Atras", fr="Retour"),
    "Costumes in Game": Translation(en="Costumes in Game", es="Personalizaciones en el juego", fr="Costumes dans le jeu"),
    "Do you want a profile picture?": Translation(en="Do you want a profile picture?", es="Deseas foto de perfil?", fr="Voulez-vous une photo de profil?"),
    "Select your scenario": Translation(en="Select your scenario", es="Selecciona tu escenario", fr="Sélectionnez votre scénario"),
    "Personalization is a unique feature for gold members ": Translation(en="Personalization is a unique feature for gold members, that can be select scenary, block texture and music ", es="La personalización es una característica única para los miembros gold, donde podra elegir el escenario, la textura de los bloques y la musica de fondo", fr="La personnalisation est une fonctionnalité unique pour les membres or"),
    "Select your texture": Translation(en="Select your texture pack", es="Selecciona tu pack textura", fr="Sélectionnez votre texture"),
    "Music Spotify Advise": Translation(en = "In Eagle Defender you can choose your favorite music through Spotify, to do this you must have a premium Spotify account and have the program installed on your computer", es="En eagle defender podras elegir tu musica preferida a traves de spotify, para ello deberas tener una cuenta premium de spotify y tener instalado el programa en tu ordenador", fr="En eagle defender, vous pouvez choisir votre musique préférée via spotify, pour cela vous devez avoir un compte premium spotify et avoir le programme installé sur votre ordinateur"),
    "Music Spotify Advise2": Translation(en="If you dont have Spotify account you can use the defualt music", es="Si no tienes cuenta de spotify podras usar la musica por defecto", fr="Si vous n'avez pas de compte spotify, vous pouvez utiliser la musique par défaut"),
    "Select your music": Translation(en="Select your music", es="Selecciona tu musica", fr="Sélectionnez votre musique"),
    "Press here": Translation(en="Press here", es="Presiona aqui", fr="Appuyez ici"),
    "Spotify User": Translation(en="Spotify User", es="Usuario de Spotify", fr="Utilisateur Spotify"),
    "Song": Translation(en="Song", es="Cancion", fr="Chanson"),
    "Pay advise": Translation(en="The personalization of the game is a unique feature for gold members, if you want to enjoy this feature you must pay a monthly fee of 5000 ₡CR", es="La personalización del juego es una característica única para los miembros gold, si deseas disfrutar de esta característica deberas pagar una cuota mensual de 5000 ₡CR", fr="La personnalisation du jeu est une fonctionnalité unique pour les membres or, si vous souhaitez profiter de cette fonctionnalité, vous devez payer un abonnement mensuel de 5000 ₡CR"),
    "Card Number": Translation(en="Card Number", es="Numero de tarjeta", fr="Numéro de carte"),
    "Card Date": Translation(en="Card Date", es="Fecha de tarjeta", fr="Date de la carte"),
    "Card CVV": Translation(en="Card CVV", es="CVV de tarjeta", fr="CVV de la carte"),
    "Card Name": Translation(en="Card Name", es="Nombre de tarjeta", fr="Nom de la carte"),

}

#EXAMPLE Lg.dic["Login"][Lg.language]